#!/usr/bin/python3
"""module that lists all states """
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Get the command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    #connect to the MySQL server
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
    )

    #create a cursor
    cursor = db.cursor()

    #prepare the sql query 
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    #execute the query
    cursor.execute(sql_query, (state_name,))

    #fetch all the rows 
    rows = cursor.fetchall()

    #display the results
    for row in rows:
        print(row)
