#!/usr/bin/python3

"""This model contains the class definition of a City
and an instance Base = declarative_base():"""

from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer)
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

#  No need cause im already importing Base from model_state
#  Base = declarative_base()


class City(Base):
    """City class that links to the MySQL table `cities`."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)