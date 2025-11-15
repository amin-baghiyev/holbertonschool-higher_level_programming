#!/usr/bin/python3
"""Save Python objects to a JSON file"""

import json


def save_to_json_file(my_obj, filename):
    """Convert object to JSON and save to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
