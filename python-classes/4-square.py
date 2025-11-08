#!/usr/bin/python3
"""This module contains a Square class."""


class Square():
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize the class"""
        self.size = size

    def area(self):
        """Function that computes the area of the square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter for size"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """Setter for size"""
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
