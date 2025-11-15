#!/usr/bin/python3
"""Serialize a dictionary to XML and deserialize it back"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Convert a dictionary to XML and save it to a file"""
    root = ET.Element("data")
    for k, v in dictionary.items():
        child = ET.SubElement(root, k)
        child.text = str(v)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8")

def deserialize_from_xml(filename):
    """Read an XML file and convert it back to a dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
