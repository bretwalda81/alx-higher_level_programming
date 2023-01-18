#!/usr/bin/python3
'''
Take in a URL and email, send POST request
'''

if __name__ == "__main__":
    import sys
    from urllib import request, parse

    values = {'email': sys.argv[2]}
    data = parse.urlencode(values).encode()
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as res:
        print(res.read().decode('UTF-8'))
