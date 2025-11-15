#!/usr/bin/python3
"""Add command-line arguments to a JSON file"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    obj = load_from_json_file("add_item.json")
except FileNotFoundError:
    obj = []
obj += argv[1:]
save_to_json_file(obj, "add_item.json")
