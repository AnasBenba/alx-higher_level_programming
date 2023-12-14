#!/usr/bin/python3
from errno import WSAEDQUOT
import sys
import MySQLdb


def main():
    usern = sys.argv[1]
    passw = sys.argv[2]
    name = sys.argv[3]
    state = sys.argv[4]
    result = ''
    q2 = 'SELECT id FROM states WHERE name = %s'
    q = 'SELECT name FROM cities WHERE state_id = ({})'.format(q2)

    db = MySQLdb.connect(host='localhost', user=usern, passwd=passw, db=name)
    cursor = db.cursor()
    cursor.execute(q, (state,))
    rows = cursor.fetchall()

    for row in rows:
        result += row[0] + ', '
    result = result.rstrip(", ")
    print(result)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
