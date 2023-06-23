#!/usr/bin/python3
"""
    Display all values in the states table of the database hbtn_0e_0_usa
    whose nam matches supplied argument.
    Safe from MySQL injections.
    Usage: ./3-my_safe_filter_states.py <mysql username> \
                                        <mysql password> \
                                        <database name> \
                                        <state name search> \
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
