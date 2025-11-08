#!/usr/bin/python3
"""Returns a list of attributes and methods of the given object.

Args:
    obj (object): The object to look up.

Returns:
    list: List of attribute and method names of the object.
"""


def lookup(obj):
    return (dir(obj))
