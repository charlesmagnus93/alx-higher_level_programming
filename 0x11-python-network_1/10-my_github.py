#!/usr/bin/python3
"""
request github api
"""
if __name__ == "__main__":

    import sys
    import requests
    req = requests.get(
            "https://api.github.com/user",
            auth=(sys.argv[1], sys.argv[2])
        )
    print(req.json().get('id'))
