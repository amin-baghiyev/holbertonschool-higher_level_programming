#!/usr/bin/python3
"""adds the State object "Louisiana" to the database"""

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
    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print(state.id)

    session.close()
