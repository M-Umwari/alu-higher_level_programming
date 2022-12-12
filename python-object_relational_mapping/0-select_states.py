#!/usr/bin/python3

""" This script lists all states from the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    get_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3],
        charset="utf8")

    opra = get_db.cursor()
    opra.execute("SELECT * FROM states ORDER BY id ASC")

    for row in opra.fetchall():
        print(row)
    opra.close()
    get_db.close()
