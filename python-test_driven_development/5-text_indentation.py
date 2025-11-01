#!/usr/bin/python3
"""
This is the "text_indentation" module.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

    if buffer:
        print(buffer.strip(), end="")
