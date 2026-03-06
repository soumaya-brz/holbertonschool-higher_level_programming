#!/usr/bin/python3
"""Lists all cities with their state name."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Connect to DB and print cities with state names."""
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State.name, City.id, City.name)\
        .join(City, State.id == City.state_id)\
        .order_by(City.id).all()

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    session.close()


if __name__ == "__main__":
    main()
