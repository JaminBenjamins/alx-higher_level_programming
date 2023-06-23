#!/usr/bin/python3
"""
    List all state objects from database hbtn_0e_6_usa
    Usage: ./7-model_state_fetch_all.py <mysql username> \
                                        <mysql password> \
                                        <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
    )
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State).order_by(State.id):
        print("{}:{}".format(state.id, state.name))
