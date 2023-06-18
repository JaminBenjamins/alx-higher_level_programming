#!/usr/bin/python3
"""
    List all city objects from the database hbtn_0e_101_usa
    Usage: ./102-relationship_cities_states_list.py <mysql username> \
                                                    <mysql password> \
                                                    <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3])
                            pool_pre_ping=True)
    session_maker = sessionmaker()
    session = session_maker()

    for city in session.query(City).order_by(City.id):
        print("{}:{} -> {}".format(city.id, city.name, city.state.name))
