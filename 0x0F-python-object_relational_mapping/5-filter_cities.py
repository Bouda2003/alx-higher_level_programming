#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <username> <pass> <db_name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    DB = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    Cursor = DB.cursor()
    Cursor.execute("SELECT * FROM `cities` \
                INNER JOIN `states` \
                   ON `cities`.`state_id` = `states`.`id` \
                ORDER BY `cities`.`id`")
    states = Cursor.fetchall()
    print(", ".join([ct[2] for ct in states if ct[4] == sys.argv[4]]))
