#!/usr/bin/python3
"""
script that prints all objects with letter a from the database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql username> /
                                   <mysql password> /
                                   <database name>
                                   <state name searched>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
