#!/usr/bin/python3

"""This model contains the class definition of a State
and an instance Base = declarative_base():"""

from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer)
from sqlalchemy.ext.declarative import declarative_base

#  Define the base class for ORM models
Base = declarative_base()


class State (Base):
    """State class that links to the MySQL table `states`."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


db_url = "sqlite://"
engine = create_engine(db_url)

# Create all tables
Base.metadata.create_all(engine)
