#!/usr/bin/python3
"""
request package error
"""
if __name__ == "__main__":

    import sys
    import requests

    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
