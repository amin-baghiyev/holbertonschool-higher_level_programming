#!/usr/bin/python3
"""CustomObject class with pickle serialization and deserialization"""
import pickle


class CustomObject():
    """Represent a custom object with name, age, and is_student attributes"""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print all attributes of the object"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject from a pickle file"""
        with open(filename, 'rb') as f:
            return (pickle.load(f))
