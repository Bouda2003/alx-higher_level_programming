#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
import urllib.request as req
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    request = req.Request(url)
    with req.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
