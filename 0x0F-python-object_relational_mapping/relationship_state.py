#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for the
'states' table in a MySQL database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,
                        Integer,
                        String)
from sqlalchemy.orm import relationship
from sys import argv
Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete', backref='states')
