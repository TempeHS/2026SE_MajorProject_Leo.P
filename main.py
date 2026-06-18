from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import jsonify
from flask import url_for
from flask import session
from flask import flash
import requests
from flask_wtf import CSRFProtect
from flask_csp.csp import csp_header

from flask_session import Session
import logging

import userManagement as dbHandler

import pyotp
import pyqrcode
import os
import base64
from io import BytesIO

# Code snippet for logging a message
# app.logger.critical("message")

app_log = logging.getLogger(__name__)
logging.basicConfig(
    filename="security_log.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
)

# Generate a unique basic 16 key: https://acte.ltd/utils/randomkeygen
app = Flask(__name__)
app.secret_key = b"_53oi3uriq9pifpff;apl"

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SESSION_FILE_DIR"] = "./flask_session"
app.config["PERMANENT_SESSION_LIFETIME"] = 2700

app.config["SESSION_REFRESH_EACH_REQUEST"]

Session(app)

csrf = CSRFProtect(app)


# Redirect index.html to domain root for consistent UX
@app.route("/index", methods=["GET"])
@app.route("/index.htm", methods=["GET"])
@app.route("/index.asp", methods=["GET"])
@app.route("/index.php", methods=["GET"])
@app.route("/index.html", methods=["GET"])
def root():
    return redirect("/", 302)


@app.route("/", methods=["GET"])
@csp_header(
    {
        # Server Side CSP is consistent with meta CSP in layout.html
        "base-uri": "'self'",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "'self' data:",
        "media-src": "'self'",
        "font-src": "'self'",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
    }
)
def index():
    return render_template("/index.html")


@app.route("/login.html", methods=["GET", "POST"])
@csp_header(
    {
        "base-uri": "'self'",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "'self' data:",
        "media-src": "'self'",
        "font-src": "'self'",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
    }
)
def login():
    if session.get("logged_in"):
        return redirect("/home.html", code=303)  # this might be wrong
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if not dbHandler.userExists(email):
            flash("Account not found. Please sign up first.", "not-registered")
            app_log.info("%s attempted to log in without registered account.", email)
            return redirect("/login.html")

        if dbHandler.getUsers(email, password):
            session["user_email"] = email
            session["user_secret"] = dbHandler.getUserSecret(email)

            app_log.info("%s has logged in.", email)
            return redirect("/2fa.html", code=303)

        flash("Incorrect email or password. Please try again.", "error")
        app_log.info("%s failed to log in.", email)
        return redirect("/login.html", code=303)

    return render_template("/login.html")


@app.route("/signup.html", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        exists = dbHandler.insertSignup(email, password)
        if not exists:
            flash("Email already registered. Please log in instead.", "error")
            return redirect("/signup.html", code=303)

        app_log.info(f"Form submitted: {email}")
        flash("Account created successfully. Please log in.", "success")
        return redirect("/login.html", code=303)

    return render_template("/signup.html")


# example CSRF protected form
@app.route("/form.html", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        app_log.info(f"Form submitted: {email}")
        return redirect("/home.html", code=303)
    else:
        return render_template("/form.html")


# Endpoint for logging CSP violations
@app.route("/csp_report", methods=["POST"])
@csrf.exempt
def csp_report():
    app.logger.critical(request.data.decode())
    return "done"


# Home page
@app.route("/home.html", methods=["GET"])
def home():
    if not session.get("logged_in"):
        app_log.warning("Unauthorised attempt to access data")
        return redirect("/", code=303)

    return render_template("/home.html")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    email = session.get("user_email", "Unknown")
    session.clear()
    app_log.info("%s logged out.", email)
    return redirect("/", code=303)


@app.route("/2fa.html", methods=["POST", "GET"])
@csp_header(
    {
        "base-uri": "'self'",
        "default-src": "'self'",
        "style-src": "'self' 'unsafe-inline'",
        "script-src": "'self'",
        "img-src": "'self' data:",
        "media-src": "'self'",
        "font-src": "'self'",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "manifest-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
    }
)
def reach_2fa():
    username = session.get("user_email", "User")
    user_secret = session.get("user_secret")

    if not user_secret:
        return redirect("/", code=303)

    totp = pyotp.TOTP(user_secret)
    otp_uri = totp.provisioning_uri(name=username, issuer_name="OneLink: HSC")
    qr_code = pyqrcode.create(otp_uri)
    stream = BytesIO()
    qr_code.png(stream, scale=10)
    qr_code_b64 = base64.b64encode(stream.getvalue()).decode("utf-8")

    if request.method == "POST":
        otp_input = request.form["otp"]
        if totp.verify(otp_input, valid_window=1):
            session["logged_in"] = True
            return redirect("/")
        else:
            flash("Invalid OTP. Please try again.", "error")
            return redirect("/2fa.html", code=303)

    return render_template("/2fa.html", qr_code=qr_code_b64, value=username)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


### Card pages
@app.route("/resources")
def resources():
    return render_template("cards/resources.html")


@app.route("/past_papers")
def past_papers():
    return render_template("cards/past_papers.html")


@app.route("/useful_websites")
def useful_websites():
    return render_template("cards/useful_websites.html")


@app.route("/personal_dashboard")
def personal_dashboard():
    return render_template("cards/personal_dashboard.html")


### Subjects
#### HSIE
@app.route("/subject/hsie/business-studies")
def businessStudies():
    return render_template("subject/hsie/business-studies.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
