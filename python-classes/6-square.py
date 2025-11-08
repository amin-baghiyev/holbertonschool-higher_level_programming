#!/usr/bin/python3
"""This module contains a Square class."""


class Square():
    """A class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the class"""
        self.size = size
        self.position = position

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

    def my_print(self):
        """Prints square"""
        if (self.size == 0):
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    @property
    def position(self):
        """Getter for position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (not isinstance(value, tuple) or
                not (value[0] >= 0 and value[1] >= 0) or
                len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
