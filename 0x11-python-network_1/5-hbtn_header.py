#!/usr/bin/python3
"""
request header
"""
if __name__ == "__main__":
    import sys
    import requests

    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
