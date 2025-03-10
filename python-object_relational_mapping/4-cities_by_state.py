#!/usr/bin/python3

"""  lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys


def list_states():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM cities"

    cur.execute(query)

    cities = cur.fetchall()

    for citie in cities:
        print(citie)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
