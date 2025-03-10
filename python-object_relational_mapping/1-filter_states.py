#!/usr/bin/python3

"""This module lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_states():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name ='{}'ORDER BY states.id ASC".format(state_name))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
