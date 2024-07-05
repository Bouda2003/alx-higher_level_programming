#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.request as req
import urllib.parse as par
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = par.urlencode(value).encode("ascii")

    request = req.Request(url, data)
    with req.urlopen(request) as response:
        print(response.read().decode("utf-8"))
