#!/usr/bin/python3
"""
    Defines a city class that inherits from base
    of the sqlalchemy linka to table cities
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        Represent a city from mysql database

    Attributes:
            id(str): The id of the city
            name(string): Name of the city
            state_id(integer): City's state id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
