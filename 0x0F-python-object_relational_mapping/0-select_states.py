#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> <pass> <db_name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    DB = MySQLdb.connect(user=sys.argv[1],password=sys.argv[2],database=sys.argv[3])
    Cursor = DB.cursor()
    Cursor.execute("SELECT * FROM `states`")
    [print(state) for state in Cursor.fetchall()]
