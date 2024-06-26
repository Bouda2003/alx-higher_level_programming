#!/usr/bin/python3
"""
creating state model useing sqlAlchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state for a mysql DB
    __tablename__ (str): the name of mysql table
    id (Integer): the state's id
    name (str): the state's name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
