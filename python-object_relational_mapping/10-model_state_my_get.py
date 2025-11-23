#!/usr/bin/python3
"""prints the State object with the name passed as argument from database"""

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
    state = (
        session.query(State)
        .filter(State.name == argv[4])
        .first()
    )
    if (state is None):
        print("Not found")
    else:
        print(state.id)

    session.close()
