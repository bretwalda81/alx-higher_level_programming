#!/usr/bin/python3
""" Importing """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
""" 8-model_state_fetch_first.py """


def listStateObj():
    """
    Class that lists only the first states in the given database
    using SQLALchemy. If the database is empty, print 'Nothing'
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    first_state = my_session.query(State).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    my_session.close()

if __name__ == '__main__':
    listStateObj()
