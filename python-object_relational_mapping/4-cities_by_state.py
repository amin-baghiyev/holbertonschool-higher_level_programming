#!/usr/bin/python3
"""script that lists all cities from the database"""

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
        "SELECT c.id, c.name, s.name FROM cities AS c \
        JOIN states AS s ON s.id = c.state_id \
        ORDER BY c.id"
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
