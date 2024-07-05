#!/usr/bin/python3
"""displays the value of the X-Request-Id variable"""
import urllib.request as req


if __name__ == "__main__":
    request = req.Request("https://alx-intranet.hbtn.io/status")
    with req.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
