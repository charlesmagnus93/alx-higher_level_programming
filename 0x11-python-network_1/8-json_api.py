#!/usr/bin/python3
"""
request POST params
"""
if __name__ == "__main__":

    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    if sys.argv[1]:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post(url, params={q: q})
    if req.headers.get('content-type') == 'application/json':
        if req.json() == {}:
            print('No result')
        else:
            print(
                '[{}] {}'
                .format(req.json().get('id'), req.json().get('name'))
            )
    else:
        print('Not a valid JSON')
