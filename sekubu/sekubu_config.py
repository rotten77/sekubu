import xml.etree.ElementTree as ET

def sekubu_config(file_path: str, attribute: str, value: str):
    tree = ET.parse(file_path)
    root = tree.getroot()
    root.set(attribute, value)
    tree.write(file_path)
        