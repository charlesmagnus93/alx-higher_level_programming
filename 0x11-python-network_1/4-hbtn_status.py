#!/usr/bin/python3
# requests module

import requests

req = requests.get('https://alx-intranet.hbtn.io/status')

print(
    'Body response:\n\t- type: {}\n\t- content: {}'
    .format(type(req.text), req.text)
)

if __name__ == "__main__":
    requests
