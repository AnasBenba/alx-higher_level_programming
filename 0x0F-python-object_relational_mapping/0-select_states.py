#!/usr/bin/python3
import sys
import MySQLdb


def main():
    usern = sys.argv[1]
    passw = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=usern, passwd=passw, db=name)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()