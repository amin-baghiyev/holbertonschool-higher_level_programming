#!/usr/bin/python3
"""prints all City objects from the database"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    query = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )
    for state, city in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
