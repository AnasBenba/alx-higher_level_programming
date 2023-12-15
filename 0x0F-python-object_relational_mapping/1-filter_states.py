#!/usr/bin/python3
"""
 connect to MySQL database and retrieves data from the table

 Usage:
 ./1-filter_states.py <username> <password> <database_name>

 Args:
 - sys.argv[1]: MySQL username
 - sys.argv[2]: MySQL password
 - sys.argv[3]: MySQL database name

 print states with a name starts with upper N
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
