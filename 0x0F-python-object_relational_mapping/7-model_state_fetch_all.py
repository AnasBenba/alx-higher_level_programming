#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def main():
    """Main function to connect to the database"""
    text = f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    Base.metadata.create_all(engine)
    engine = create_engine(text)
    session = Session(engine)
    result = session.query(State).order_by(State.id.asc()).all()
    for r in result:
        print(f'{r.id}: {r.name}')
    session.close()


if __name__ == "__main__":
    main()
