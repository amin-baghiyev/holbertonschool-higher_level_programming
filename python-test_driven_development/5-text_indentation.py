#!/usr/bin/python3
"""
This is the "text_indentation" module.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', and ':'. No leading/trailing spaces."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = {'.', '?', ':'}
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    remainder = text[start:].strip()
    if remainder:
        print(remainder, end='')
