#!/usr/bin/python3
"""
Request to DB using argements & filter
"""
from sys import argv
import MySQLdb


def main():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "[N]%" ORDER BY id ASC')
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
