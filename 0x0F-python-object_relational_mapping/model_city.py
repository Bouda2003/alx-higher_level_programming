#!/usr/bin/python3
"""
Defines a City model
Inherits from SQLAlchemy Base and links to mysql cities's table
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city in MYsql database
    id(int): city's id
    name(String): city's name
    state_id(int): ForeignKey represents state_id
    """
    __table__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
