#!/usr/bin/python3
"""
import file
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    class definiftion
    """

    __table__ = 'states'

    id = Column(Integer, primary_key=True, nuliable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
