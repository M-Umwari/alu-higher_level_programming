#!/usr/bin/python3
""" module listing states
from the database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # port and host are default local and 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY \
        states.id ASC""".format(argv[4]))
    result = cur.fetchall()
    # display elements with N
    # only by taking comparing their first letter in tuple
    for a in result:
        if a[1][0] == 'N':
            print(a)
    # close cursor and db
    cur.close()
    db.close()

