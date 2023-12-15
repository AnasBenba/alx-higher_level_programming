#!/usr/bin/python3
"""
Connects to a MySQL database and retrieves data from the 'states' table.

Usage:
./0-select_states.py <username> <password> <database_name>

Args:
- sys.argv[1]: MySQL username
- sys.argv[2]: MySQL password
- sys.argv[3]: MySQL database name

Prints the rows from the 'states' table ordered by the 'id' column.
"""

import sys
import MySQLdb


def main():
    """
    Main function to connect to the database and retrieve
    data from the 'states' table
    """
    usern = sys.argv[1]
    passw = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect('localhost', usern, passw, name, 3306)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
