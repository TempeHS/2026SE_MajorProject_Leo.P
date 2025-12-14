import sqlite3 as sql
import bcrypt


def getUsers(email, password):
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM user_info WHERE email = ? AND password = ?", (email, password)
    )
    result = cur.fetchone()
    con.close()
    if result is None:
        return False
    else:
        return True


def insertSignup(email, password):
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO user_info (email, password) VALUES (?,?)", (email, password)
    )
    con.commit()
