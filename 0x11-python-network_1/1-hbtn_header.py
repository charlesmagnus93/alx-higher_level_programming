#!/usr/bin/python3

import sys
import urllib.request


def main():
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))


if __name__ == '__main__':
    main()
