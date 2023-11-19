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
    Change the name of a State object in the database
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_change = session.query(State).filter_by(id=2).first()

    if state_to_change:
        state_to_change.name = 'New Mexico'
        session.commit()
    else:
        print("State with ID=2 not found")

    session.close()
