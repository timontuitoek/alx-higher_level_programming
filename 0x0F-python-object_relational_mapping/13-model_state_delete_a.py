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
    Delete State objects from the database based on a condition
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = session.query(State)
    .filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()
