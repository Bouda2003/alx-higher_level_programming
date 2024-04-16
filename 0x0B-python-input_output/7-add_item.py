#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_to_list_and_save(args):
    file_name = "add_item.json"
    try:
        data = load_from_json_file(file_name)
    except FileNotFoundError:
        data = []
    data.extend(args)
    save_to_json_file(data, file_name)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_to_list_and_save(args)
