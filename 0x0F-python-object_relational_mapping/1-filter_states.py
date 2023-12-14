#!/usr/bin/python3

import sys
import MySQLdb


def main():
    usern = sys.argv[1]
    passw = sys.argv[2]
    name = sys.argv[3]
    q = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"

    db = MySQLdb.connect(host='localhost', user=usern, passwd=passw, db=name)
    cursor = db.cursor()
    cursor.execute(q)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()