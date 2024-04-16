#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_to_list_and_save(args):
    file_name = "add_item.json"
    if path.exists(file_name):
        data = load_from_json_file(file_name)
    else:
        data = []
    data.extend(args)
    save_to_json_file(data, file_name)
    print("Arguments added to the list and saved to", file_name)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_to_list_and_save(args)
