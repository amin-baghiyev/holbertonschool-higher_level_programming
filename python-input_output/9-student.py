#!/usr/bin/python3
"""Define a Student class with JSON serialization"""


class Student():
    """Represent a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of the Student"""
        return (self.__dict__)
