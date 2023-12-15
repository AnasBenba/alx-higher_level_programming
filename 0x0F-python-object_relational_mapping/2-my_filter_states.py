#!/usr/bin/python3
"""
 connect to MySQL database and retrieves data from the table

 Usage:
 ./1-filter_states.py <username> <password> <database_name> <name_searched>

 Args:
 - sys.argv[1]: MySQL username
 - sys.argv[2]: MySQL password
 - sys.argv[3]: MySQL database name
 - sys.argv[4]: state name searched

 print states where a name matches the argument
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
    searched = sys.argv[4]
    q2 = 'ORDER BY states.id'
    q = "SELECT * FROM states WHERE name = '{}' {}".format(searched, q2)

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
