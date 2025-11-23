#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
that is safe from MySQL injections
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
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id",
        (argv[4],)
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
