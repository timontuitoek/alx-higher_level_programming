#!/usr/bin/python3
"""
import file
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306)

    cur = db.cursor()
    match = argv[4]
    cur.execute("SELECT * FROM states \
            WHERE name LIKE %s \
            ORDER BY states.id ASC" (match, ))

    rows = cur.fetchall()

    for row in rows:
        print(row)
