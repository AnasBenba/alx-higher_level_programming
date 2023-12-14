#!/usr/bin/python3
import sys
import MySQLdb


def main():
    usern = sys.argv[1]
    passw = sys.argv[2]
    name = sys.argv[3]
    q2 = "LEFT JOIN states ON state_id = states.id ORDER BY cities.id"
    q = "SELECT cities.id, cities.name, states.name FROM cities {}".format(q2)

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
