#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from unittest import result
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    data_URL = f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(data_URL)
    session = Session(engine)
    result = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in result:
        print(f"{State.name}: ({city.id}) {City.name}")
