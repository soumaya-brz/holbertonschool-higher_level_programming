#!/usr/bin/python3
"""Lists states matching user input (safe from SQL injection)."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and safely filter states by name."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (searched,))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
