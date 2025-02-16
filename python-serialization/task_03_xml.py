#!/usr/bin/python3

"""
This module contains two functions to data
Serialize and Deserialize using XML
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    
    root = ET.Element("data")

    for key, val in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = val
    
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    new_dict = {child.tag: child.attrib for child in root}
    return new_dict
