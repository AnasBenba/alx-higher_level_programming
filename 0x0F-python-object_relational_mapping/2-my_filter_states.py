#!/usr/bin/python3
import sys
import MySQLdb


def main():
    usern = sys.argv[1]
    passw = sys.argv[2]
    name = sys.argv[3]
    searched = sys.argv[4]
    q = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id".format(searched)

    db = MySQLdb.connect(host="localhost", user=usern, passwd=passw, db=name)
    cursor = db.cursor()
    cursor.execute(q)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
