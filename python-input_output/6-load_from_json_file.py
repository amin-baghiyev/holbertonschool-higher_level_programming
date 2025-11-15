#!/usr/bin/python3
"""Load a Python object from a JSON file"""

import json


def load_from_json_file(filename):
    """Read JSON from file and convert to Python object"""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.loads(f.read()))
