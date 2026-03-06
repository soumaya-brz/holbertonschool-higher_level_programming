#!/usr/bin/python3
"""Lists all cities of a given state (SQL injection safe)."""

import MySQLdb
import sys


def main():
    """Connect to MySQL and list cities for the given state."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    """

    cursor.execute(query, (state,))

    result = cursor.fetchone()

    if result and result[0]:
        print(result[0])

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
