#!/usr/bin/python3

""" Prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db_url = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_url)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # state = session.query(State).filter(State.name == state_name).first()
    state = session.query(State).get({"name":f"{state_name}"}).first()
    if state:
        print(state.id)
    else: 
        print("Not found")

    session.close()
