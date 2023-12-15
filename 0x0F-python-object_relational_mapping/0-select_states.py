#!/usr/bin/python3
import sys
import MySQLdb


def main():
    """
    connect to a Mysql database and retrives data from the 'states' table.
    Usage:
    python3 0-select_states.py <username> <password> <database>

    Args:
    usern = username
    passw = password
    name = database

    print the row from 'states' orderd by id column
    """
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
