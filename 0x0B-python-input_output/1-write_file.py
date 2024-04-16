#!/usr/bin/python3
"""Defines a line counting function"""


def write_file(filename="", text=""):
    """return the number of lines in the text"""
    li = 0
    with open(filename) as f:
        for li in f:
            li += 1
        return li
