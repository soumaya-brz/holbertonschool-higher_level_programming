#!/usr/bin/python3
"""Insert Louisiana into the database and print its id."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to MySQL, insert Louisiana and print new id."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State object
    new_state = State(name="Louisiana")

    # Add and commit to database
    session.add(new_state)
    session.commit()

    # Print new id
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    main()
