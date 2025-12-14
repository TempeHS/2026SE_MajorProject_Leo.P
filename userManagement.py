import sqlite3 as sql
import bcrypt


### example
def getUsers():
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM user_info  ")
    con.close()
    return cur


def insertSignup(email, password):
    con = sql.connect("databaseFiles/database.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO user_info (email, password) VALUES (?,?)", (email, password)
    )
    con.commit()
