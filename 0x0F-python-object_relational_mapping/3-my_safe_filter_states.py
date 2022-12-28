#!/usr/bin/python3
""" Importing MySQLdb for database tasks. Sys is for retrieving
    command line arguments """
import MySQLdb
import sys
""" 3-my_safe_filter_states.py """


def getStates():
    """
    Driving function. Actually not necessary, but done to make
    the entire code nicer to read.
    Accesses the database with user and password, all passed in,
    to localhost at port 3306. Then, retrieve all information
    from the states database and prints out only those that match
    the user's input at argument 4
    By making a small change, this script also protects against
    an SQL injection that may cause undesirable results
    """
    mydb = MySQLdb.connect(host='localhost',
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states WHERE name = %s \
                      ORDER BY states.id", (sys.argv[4],))
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

if __name__ == '__main__':
    getStates()
