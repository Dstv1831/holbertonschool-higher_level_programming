#!/usr/bin/python3

"""This model contains the class definition of a State
and an instance Base = declarative_base():"""

from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer)
from sqlalchemy.ext.declarative import declarative_base


db_url = "sqlite://"
engine = create_engine(db_url)
Base = declarative_base()

class State (Base):
    
    """ Class state that inherits from Base
    
    Attriibutes:
        id: INT primary Key
        name: STRING max of 128 char"
        """
    
    __tablename__ = 'state_table'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

Base.metadata.create_all(engine)


