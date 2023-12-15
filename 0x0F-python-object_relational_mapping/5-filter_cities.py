#!/usr/bin/python3
"""
 connect to MySQL database and retrieves data from the table

 Usage:
 ./1-filter_states.py <username> <password> <database_name>
 <state name>

 Args:
 - sys.argv[1]: MySQL username
 - sys.argv[2]: MySQL password
 - sys.argv[3]: MySQL database name
 - sys.argv[4]: state name

 print cities from the database
"""

import sys
import MySQLdb


def main():
    """
    Main function to connect to the database and retrieve
    data from the 'cities' table
    """
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
