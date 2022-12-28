#!/usr/bin/python3
""" Importing """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
""" 13-model_state_delete_a.py """


def listStateObj():
    """
    Class that deletes all states in the given database with the
    letter 'a' using SQLALchemy
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    no_a_state = my_session.query(State).filter(State.name.contains('a'))
    for x in no_a_state:
        my_session.delete(x)

    my_session.commit()

    my_session.close()

if __name__ == '__main__':
    listStateObj()
