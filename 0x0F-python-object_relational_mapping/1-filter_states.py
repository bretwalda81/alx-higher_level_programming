#!/usr/bin/python3
""" Importing MySQLdb for database tasks. Sys is for retrieving
    command line arguments """
import MySQLdb
import sys
""" 1-filter_states.py """


def getStates():
    """
    Driving function. Actually not necessary, but done to make
    the entire code nicer to read.
    Accesses the database with user and password, all passed in,
    to localhost at port 3306. Then, retrieve all information
    from the states database that starts with the letter 'N' and
    prints them all out
    """
    mydb = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE 'N%' \
                      ORDER BY states.id")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

if __name__ == '__main__':
    getStates()
