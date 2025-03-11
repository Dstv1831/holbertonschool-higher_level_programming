#!/usr/bin/python3

"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    

db_url = "sqlite://"
engine = create_engine(db_url)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).all

for state in states:
    print(f"{states.id}: {state.name}")

session.close()

if __name__=="__main__":
    list_states()