!/usr/bin/python3
""" Get the status of a specific website. Requests package version """
import requests


def print_status():
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))

if __name__ == '__main__':
    print_status()
