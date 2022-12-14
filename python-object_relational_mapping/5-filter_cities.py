#!/usr/bin/python3

"""module list states from database"""

import MySQLdb

if __name__ == "__main__":

    from sys import argv
    # port and host are default local and 3306
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # link both tables and get base on state_id
    # vert input against sql injection
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC""", (argv[4],))
    result = cur.fetchall()
    # check if cities pass
    # the argument check and add to list
    # with csv formating style
    cities = []
    for a in result:
        if a[2] == argv[4]:
            cities.append(a[1])
    print(', '.join(cities))
    # close cursor and db
    cur.close()
    db.close()
