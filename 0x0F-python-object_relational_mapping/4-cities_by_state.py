#!/usr/bin/python3
""" Importing MySQLdb for database tasks. Sys is for retrieving
    command line arguments """
import MySQLdb
import sys
""" 4-cities_by_state.py """


def getCities():
    """
    Driving function. Actually not necessary, but done to make
    the entire code nicer to read.
    Access the database with user and password, all passed in,
    to localhost at port 3306. Then, merge the two databases
    cities and states into one table, and retrieve cities.id,
    name of city, and name of state. Print them all out
    """
    mydb = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    mycursor = mydb.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM states \
           LEFT JOIN cities ON states.id = state_id \
           ORDER BY cities.id"
    mycursor.execute(cmd)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

if __name__ == '__main__':
    getCities()
