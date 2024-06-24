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
    Cursor.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                 FROM `cities` \
                INNER JOIN `states` \
                   ON `cities`.`state_id` = `states`.`id` \
                ORDER BY `cities`.`id`")
    states = Cursor.fetchall()
    for state in states:
        print(state)
