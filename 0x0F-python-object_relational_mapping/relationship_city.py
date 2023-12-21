#!/usr/bin/python3
"""the class definition of a City"""
from model_state import Base
from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey)


class City(Base):
    """
    Represents a city in the database.

    Attributes:
        id (int): The unique identifier for the city.
        name (str): The name of the city.
        state_id (str): The id of the state
    """
    __tablename__ = "cities"
    id = Column(autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
