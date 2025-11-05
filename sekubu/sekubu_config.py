import xml.etree.ElementTree as ET

def sekubu_config(file_path: str, config: dict):
    with open(file_path, encoding='utf-8') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        for attribute, value in config.items():
            root.set(attribute, value)
        tree.write(file_path, encoding='utf-8', xml_declaration=True, short_empty_elements=False)
