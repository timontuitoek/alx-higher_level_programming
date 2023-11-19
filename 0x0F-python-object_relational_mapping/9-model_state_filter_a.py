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
    Access the database and get the states with letter 'a'
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%'))
    .order_by(State.id)

    for state in states_with_a:
        print('{}: {}'.format(state.id, state.name))
