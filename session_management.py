from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
SESSION_TYPE = "filesystem"
app.config.from_object(__name__)
Session(app)


@app.route("/set/<string:value>")
def set_session(value):
    session["key"] = value
    return "<h1>Code 200 okay</h1>"


@app.route("/get/")
def get_session():
    stored_session = session.get("key", "No session was set")
    return f"<h3>{stored_session}</h3>"


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
