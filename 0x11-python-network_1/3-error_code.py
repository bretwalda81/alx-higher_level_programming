#!/usr/bin/python3
'''
Take in a URL, send a request to URL, and dispaly body
'''
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            html = res.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as er:
        print("Error code: {}".format(er.code))
