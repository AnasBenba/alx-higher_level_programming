#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    text = f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(text)
    session = Session(engine)
    result = session.query(State).order_by(State.id).all()
    for r in result:
        print(f'{r.id}: {r.name}')
