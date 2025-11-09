#!/usr/bin/python3
"""This module contains a BaseGeometry class."""


class BaseGeometry():
    """A class that represents a geometric shapes."""

    def area(self):
        """Function that computes the area of the shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value"""
        if (not isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
