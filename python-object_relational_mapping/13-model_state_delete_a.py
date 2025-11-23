#!/usr/bin/python3
"""deletes all State objects with name containing the letter a from database"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
    ))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    states = (
        session.query(State)
        .filter(State.name.contains('a'))
        .all()
    )
    for state in states:
        session.delete(state)
    session.commit()

    session.close()
