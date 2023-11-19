#!/usr/bin/python3
"""
import file
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and get the State with the given name
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_name = argv[4]
    result = session.query(State).filter(State.name == state_name).first()

    if result is not None:
        print(result.id)
    else:
        print("Not found")
