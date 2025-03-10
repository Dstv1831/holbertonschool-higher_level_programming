#!/usr/bin/python3

""" This modeule takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa """

import MySQLdb
import sys


def list_states():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities INNER JOIN states on\
        cities.state_id = states.id WHERE states.name = %s"

    cur.execute(query, (state,))

    cities = cur.fetchall()

    for citie in cities:
        print(citie)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
