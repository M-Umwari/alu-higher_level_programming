#!/usr/bin/python3
""" this is module list that states
from database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # port and host are default local and 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # vert input from users
    # use string formating to be specific
    cur.execute("SELECT * FROM states WHERE states.name = %s\
    ORDER BY states.id ASC", (argv[4],))
    result = cur.fetchall()
    # check if second argument of tuple
    # is same as the passed argument
    for a in result:
        print(a)
    # close cursor and db
    cur.close()
    db.close()
