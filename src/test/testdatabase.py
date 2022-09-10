import json
import sqlite3

conn = sqlite3.connect("assets/database.db")
cur = conn.cursor()

while True:
    i = input("> ")

    if i is ":quit":
        conn.commit()
        conn.close()
        break

#    res = cur.execute("SELECT * FROM")