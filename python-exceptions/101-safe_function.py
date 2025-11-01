#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    try:
        r = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        r = None
    return (r)
