#!/usr/bin/python3

""" Prints all City objects from the 
database hbtn_0e_14_usa:"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_url = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_url)

    # create a Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # this will return tuples insted of just one object, same as this:
    # SELECT cities.id, cities.name, states.name
    # FROM cities
    # JOIN states ON cities.state_id = states.id
    # ORDER BY cities.id;
    cities = session.query(City, State.name).join(State).order_by(City.id).all()

    for city, state_name in cities:
        print(f"{state_name}: ({city.id}) {city.name}") 
    
    session.close()
