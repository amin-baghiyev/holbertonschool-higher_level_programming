#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1], passwd=argv[2], db=argv[3],
        port=3306
    )
    cursor = db.cursor()

    cursor.execute(
        "SELECT c.name FROM cities AS c \
        JOIN states AS s ON s.id = c.state_id \
        WHERE BINARY s.name = %s \
        ORDER BY c.id",
        (argv[4],)
    )

    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cursor.close()
    db.close()
