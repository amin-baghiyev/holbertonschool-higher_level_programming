#!/usr/bin/python3
"""This module contains a Square class."""


class Square():
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize the class"""
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Function that computes the area of the square"""
        return (self.__size * self.__size)
