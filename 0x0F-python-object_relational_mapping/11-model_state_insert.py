#!/usr/bin/python3
""" Importing """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
""" 11-model_state_insert.py """


def listStateObj():
    """
    Class that adds stuff to the given database using SQLAlchemy
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    Louisiana = State(name='Louisiana')
    my_session.add(Louisiana)
    my_session.commit()

    print(Louisiana.id)

    my_session.close()

if __name__ == '__main__':
    listStateObj()
