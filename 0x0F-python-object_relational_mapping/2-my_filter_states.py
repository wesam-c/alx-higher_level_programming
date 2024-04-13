#!/usr/bin/python3
"""module that takes in an argument & displays all values  matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials from Comm. Line Args
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    #execute the SQL query to reach all states with specified name
    cursor.execute("SELECT * \
                   FROM `states` \
                    WHERE BINARY `name` = '{}".format(sys.argv[4]))
    
    # Fetch all rows and print the states
    [print(state) for state in cursor.fetchall()]