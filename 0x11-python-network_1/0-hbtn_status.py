#!/usr/bin/python3
""" Get the status of a specific website """
import urllib.request


def printStatus():
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as req:
        printme = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(printme)))
        print("\t- content: {}".format(printme))
        print("\t- utf8 content: {}".format(printme.decode('utf-8')))


if __name__ == '__main__':
    printStatus()
