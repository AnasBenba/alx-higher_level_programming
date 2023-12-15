#!/usr/bin/python3
"""list first State objects from the database hbtn_0e_6_usa"""
from ast import arg
from sys import argv
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    data_URL = f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(data_URL)
    Base.metadata.create_all(engine)
    session = Session(engine)
    result = session.query(State).order_by(State.id.asc()).first()
    if result is not None:
        print(f'{result.id}: {result.name}')
    else:
        print('Nothing')
    session.close()
