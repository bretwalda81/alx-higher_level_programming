#!/usr/bin/python3

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def listStateObj():
    """
    Class that lists all cities by state in the given database.
    The equivalent to using JOIN in SQL, this is done using sqlalchemy
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    city_state = my_session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for x in city_state:
        print("{}: ({}) {}".format(x.State.name, x.City.id, x.City.name))

    my_session.close()

if __name__ == '__main__':
    listStateObj()
