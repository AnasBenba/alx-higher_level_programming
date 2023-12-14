#!/usr/bin/python3
import sys
import MySQLdb
try:
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect(host = 'localhost', port = 3306, user = username, passwd = password, db = name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
except MySQLdb.Error as e:
    print("MySQL Error:", e)