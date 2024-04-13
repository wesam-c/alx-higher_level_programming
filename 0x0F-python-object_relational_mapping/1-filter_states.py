#!/usr/bin/python3
"""module that lists states that starts with N"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from Comm. Line Args
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    #execute the SQL query to reach all states stored by id
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
