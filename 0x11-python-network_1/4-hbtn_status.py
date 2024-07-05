#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests as req


if __name__ == "__main__":
    request = req.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(request.text))
    print("\t- content: {}".format(request.text))
