#!/usr/bin/python3
import sys
import MySQLdb


def main():
    """
    Connects to a MySQL database and retrieves data from the 'states' table.

    Usage:
    python script_name.py <username> <password> <database_name>

    Args:
    - sys.argv[1]: MySQL username
    - sys.argv[2]: MySQL password
    - sys.argv[3]: MySQL database name

    Prints the rows from the 'states' table ordered by the 'id' column.
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
