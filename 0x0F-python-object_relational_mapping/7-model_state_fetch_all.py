#!/usr/bin/python3
"""Script to list all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connection setup
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print results
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
