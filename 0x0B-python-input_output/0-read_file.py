#!/usr/bin/python3
"""Defines a text reading content in files function"""


def read_file(filename=""):
    """print all the content of a file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
