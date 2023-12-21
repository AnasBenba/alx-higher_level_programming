#!/usr/bin/python3

from os import name
from re import S
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State, Base
from relationship_city import City
from sys import argv

if __name__ == "__main__":
	data_URL = f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
	engine = create_engine(data_URL)
	Base.metadata.create_all(engine)
	session = Session(engine)
	city = City(name="San Francisco")
	state = State(name="California")
	session.add(city)
	session.add(state)
	session.commit()
	session.close()
