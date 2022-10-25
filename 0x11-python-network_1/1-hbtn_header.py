#!/usr/bin/python3
"""
get header
"""
if __name__ == '__main__':
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headeirs.get('X-Request-Id'))
