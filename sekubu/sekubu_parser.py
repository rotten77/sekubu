import xml.etree.ElementTree as ET
# import PySimpleGUI as sg
import os

from sebuku_example import create_example_config

def sekubu_parser(file_path: str):

    config = {'theme': 'dark', 'width': 250, 'height': 250}

    if not os.path.exists(file_path):
        create_example_config(file_path)
    
    try:
        tree = ET.parse(file_path)
    except:
        return {'exception': f'Error parsing {file_path}', 'config': config}
        # raise Exception(f'Error parsing {file_path}')
    
    root = tree.getroot()

    # layout = []
    # layout_tabs = []
    layout = []
    # commands = {}

    if 'theme' in root.attrib:
        theme = root.get('theme').lower()
        config['theme'] = theme if theme in ['dark', 'light'] else 'dark'

    if 'width' in root.attrib:
        config['width'] = int(root.get('width')) if root.get('width').isdigit() else 250

    if 'height' in root.attrib:
        config['height'] = int(root.get('height')) if root.get('height').isdigit() else 250
  
    
    i=0
    for element in root:

        if element.tag == 'separator':
            layout.append({'type': 'separator'})
        if element.tag == 'text':
            layout.append({'type': 'text', 'content': element.text})
        if element.tag == 'button':
            i+=1
            if 'label' not in element.attrib:
                return {'exception': f'Error parsing {file_path}', 'config': config}
                # raise ValueError(f'No label found for button #{b} ')
            else:
                label = element.get('label')
            
            new_console = True
            if 'new_console' in element.attrib:
                new_console_attr = element.get('new_console').lower().strip()
                if new_console_attr == "false":
                    new_console = False


            show_output = 'never'
            if new_console == False:
                if 'show_output' in element.attrib:
                    show_output = element.get('show_output').lower().strip()
                    if show_output=='true':
                        show_output = 'always'
                    elif show_output=='false':
                        show_output = 'never'
                    if show_output not in ['never', 'always', 'if_not_empty']:
                        show_output = 'never'
            
            layout.append({'type': 'button', 'label': label, 'tag': f'button_{i}', 'command': element.text, 'new_console': new_console, 'show_output': show_output})

    return {
        'layout': layout,
        'config': config,
        'exception': ''
    }