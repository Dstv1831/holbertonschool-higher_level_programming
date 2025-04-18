#!/usr/bin/python3

""" Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_url = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_url)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(State.name.like("%a%")).all()
    print(f"Deleting {len(states)} states")

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
