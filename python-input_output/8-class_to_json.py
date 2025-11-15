#!/usr/bin/python3
"""Convert a class instance to a dictionary representation"""


def class_to_json(obj):
    """Return the dictionary representation of a class instance"""
    return (obj.__dict__)
