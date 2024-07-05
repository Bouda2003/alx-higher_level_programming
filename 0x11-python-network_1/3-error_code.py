#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.request as req
import urllib.error as err
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except err.HTTPError as e:
        print("Error code: {}".format(e.code))
