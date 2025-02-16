import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The file name where the XML will be saved.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through the dictionary and create child elements
    for key, value in dictionary.items():
        # Create a child element for each key-value pair in the dictionary
        element = ET.SubElement(root, key)
        element.text = str(value)  # Convert value to string to store in XML

    # Create an ElementTree object from the root element
    tree = ET.ElementTree(root)

    # Write the tree to the specified XML file with UTF-8 encoding and declaration
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file back into a Python dictionary.
    Args:
        filename (str): The XML file to read from.
    Returns:
        dict: The deserialized dictionary.
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Initialize an empty dictionary to hold the deserialized data
    new_dict = {}

    # Iterate through the child elements of the root
    for child in root:
        value = child.text.strip() if child.text else ""  # Handle empty text

        # Handle type conversions for numbers
        if value.isdigit():
            value = int(value)  # Convert to integer if it represents a number
        elif value.replace('.', '', 1).isdigit() and value.count('.') < 2:
            value = float(value)  # Convert to float if it represents a float

        new_dict[child.tag] = value  # Add the tag and value to the dictionary

    return new_dict
