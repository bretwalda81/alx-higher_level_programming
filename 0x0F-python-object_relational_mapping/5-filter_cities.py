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
    cities and states into one table, and retrieve all cities
    of the state given as sys.argv[4]
    """
    new_list = []

    mydb = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT cities.name FROM states \
                      LEFT JOIN cities ON states.id = state_id \
                      WHERE states.name = %s \
                      ORDER BY cities.id", (sys.argv[4],))
    myresult = mycursor.fetchall()

    for x in range(len(myresult)):
        new_list.append(myresult[x][0])
        if x != len(myresult) - 1:
            new_list.append(", ")

    print(''.join(new_list))

if __name__ == '__main__':
    getCities()
