import xml.etree.ElementTree as ET

def sekubu_config(file_path: str, config: dict):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for attribute, value in config.items():
        root.set(attribute, value)
    tree.write(file_path)
        