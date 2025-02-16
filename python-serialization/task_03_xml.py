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
        element.text = str(val)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()

    new_dict = {}

    for child in root:
        value = child.text.strip() if child.text else ""
        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
            value = float(value)

        new_dict[child.tag] = value
    return new_dict
