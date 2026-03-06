#!/usr/bin/python3
"""Delete all State objects with name containing 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to DB and delete states with 'a' in name."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).delete(
        synchronize_session=False
    )

    session.commit()
    session.close()


if __name__ == "__main__":
    main()
