#!/usr/bin/python3
"""This module contains a Rectangle class."""


class Rectangle():
    """A class that represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the class"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width"""
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that computes the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Function that computes the perimeter of the rectangle"""
        if (self.width == 0 or self.height == 0):
            return (0)
        return ((self.width + self.height) * 2)

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() < rect_2.area()):
            return (rect_2)
        else:
            return (rect_1)

    def __str__(self):
        """Returns a representation of rectangle"""
        if (self.width == 0 or self.height == 0):
            return ("")
        sym = str(self.print_symbol)
        return (((self.width * sym + '\n') * self.height)[:-1])

    def __repr__(self):
        """Return a string representation to recreate the object"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
