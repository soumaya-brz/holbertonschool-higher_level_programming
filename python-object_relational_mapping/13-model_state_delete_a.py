#!/usr/bin/python3
"""Delete all State objects with name containing 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to DB and delete states whose name contains 'a'."""
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
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
