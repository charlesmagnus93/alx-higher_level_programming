#!/usr/bin/python3
"""
Post data
"""
if __name__ == "__main__":

    import sys
    import requests

    data = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=data)
    print(req.text)
