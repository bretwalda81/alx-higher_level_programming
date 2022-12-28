#!/usr/bin/python3
""" Importing """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
""" 12-model_state_update_id_2.py """


def listStateObj():
    """
    Class that updates the name of the state associated with id 2
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    get_id = my_session.query(State).filter(State.id == 2).first()
    get_id.name = "New Mexico"
    my_session.commit()

    my_session.close()

if __name__ == '__main__':
    listStateObj()
