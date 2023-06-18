#!/usr/bin/python3
"""
    Create a state California with a city in it 
    from the database hbtn_0e_100_usa
    Usage: ./100-relationship_states_cities.py <mysql username> \
                                               <mysql password> \
                                               <database name>
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3])
                            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
