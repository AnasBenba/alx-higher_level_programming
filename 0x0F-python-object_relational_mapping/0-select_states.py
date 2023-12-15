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

    db = MySQLdb.connect('localhost', usern, passw, name, port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
