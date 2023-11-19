#!/usr/bin/python3
"""
import file
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to database
    """

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306)

    with db.cursor() as cur:
        cur.execute("""
        SELECT
            cities.id, cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
        """, {
            'state_name': argv[4]
        })

        rows = cur.fetchall()

        if rows is not None:
            for row in rows:
                print(row)
