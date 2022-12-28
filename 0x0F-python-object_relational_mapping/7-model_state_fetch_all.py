#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def listStateObj():
    """
    Class that lists all states in the given database using SQLALchemy
    Its non-SQLAlchemy variant is provided for comparison
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # The commented out code works perfectly fine and does what we want.
    # However, it does not utilize sqlalchemy so technically this is
    # incorrect
    """
    q = engine.execute('SELECT * FROM states ORDER BY states.id')
    available_tables = q.fetchall()
    for x in available_tables:
        print("{}: {}".format(x.id, x.name))
    """
    # This does use sqlalchemy, and in a way is much easier
    # Using query is very useful in future tasks where trying
    # the SQL variant... would be rather difficult
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    my_session = Session()

    for state in my_session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    my_session.close()

if __name__ == '__main__':
    listStateObj()
