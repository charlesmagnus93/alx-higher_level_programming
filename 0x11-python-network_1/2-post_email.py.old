#!/usr/bin/python3

import sys
import urllib.request

data = urllib.parse.urlencode({"email": sys.argv[2]})
data = data.encode('ascii')
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
if __name__ == '__main__':
    sys, urllib.request
