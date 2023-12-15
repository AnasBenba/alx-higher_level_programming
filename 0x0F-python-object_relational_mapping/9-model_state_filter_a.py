#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    data_URL = f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(data_URL)
    session = Session(engine)
    result = (session.query(State)
              .filter(State.name.like('%a%'))
              .order_by(State.id.asc())
              .all())
    for r in result:
        print(f'{r.id}: {r.name}')
    session.close()
