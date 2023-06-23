#!/usr/bin/python3
"""
    Define a state model that contain class definition
    of a state and instance base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class  State(Base):
    """
        Inherits from Base Tips
        links to MySQL table states
        class attribute id can't be null and is PK
        class attribute name is a string and can't be null
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
