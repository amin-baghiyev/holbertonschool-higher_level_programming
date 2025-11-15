#!/usr/bin/python3
"""Serialize Python objects to a JSON file and deserialize from it"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize `data` to JSON and save it to `filename`"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON data from `filename` and deserialize to Python object"""
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
