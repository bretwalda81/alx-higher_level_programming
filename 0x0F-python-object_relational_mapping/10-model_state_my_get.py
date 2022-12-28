#!/usr/bin/python3
""" Importing """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
""" 10-model_state_my_get.py """


def listStateObj():
    """
    Class that lists the id of the user inputted state using SQLAlchemy
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    ustate = my_session.query(State).filter(State.name == sys.argv[4]).first()
    if ustate is None:
        print("Not found")
    else:
        print("{}".format(ustate.id))

    my_session.close()

if __name__ == '__main__':
    listStateObj()
