#!/usr/bin/python3
"""
    Takes an argument and displays all values
    in the states table of a database hbtn_0e_0_usa 
    where name matches the argument
    Usage: ./2-my_filter_states.py <mysql username>
                                   <mysql password>
                                   <database name>
                                   <state name search>
"""
import sys
import MySQLdb

if __name__ = "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM statess
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    [print(state) for state in c.fetchall()]
