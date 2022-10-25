#!/usr/bin/python3
"""
get header
"""
import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
if __name__ == '__main__':
    sys, urllib.request
