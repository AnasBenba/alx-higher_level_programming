#!/usr/bin/python3
"""script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    data_URL = f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(data_URL)
    session = Session(engine)
    result = session.query(State).filter(State.name == argv[4]).all()
    if not result:
        print('Not found')
    else:
        for r in result:
            print(r.id)
    session.close()
