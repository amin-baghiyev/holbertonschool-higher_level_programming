#!/usr/bin/python3
"""Module for reading and printing a file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents."""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
