import xml.etree.ElementTree as ET
import PySimpleGUI as sg
import os

from sebuku_example import create_example_config

def sekubu_parser(file_path: str):

    if not os.path.exists(file_path):
        create_example_config(file_path)
    
    try:
        tree = ET.parse(file_path)
    except:
        raise Exception(f'Error parsing {file_path}')
    
    root = tree.getroot()

    layout = []
    layout_tabs = []
    commands = {}
    config = {}

    if 'theme' in root.attrib:
        config['theme'] = root.get('theme')
    else:
        config['theme'] = 'DarkGrey3'

    g=0;
    for group in root.findall('group'):
        group_layout = []
        g+=1
        try:
            group_name = group.find('name').text
        except:
            raise ValueError(f'No name found for group #{g}')
        
        b=0
        for element in group:

            if element.tag == 'separator':
                group_layout.append([sg.HorizontalSeparator()])
            if element.tag == 'header':
                group_layout.append([sg.Text(element.text,size=(48, 1))])
            if element.tag == 'text':
                group_layout.append([sg.Text(element.text)])
            if element.tag == 'button':
                b+=1
                if 'label' not in element.attrib:
                    raise ValueError(f'No label found for button #{b} in group {group_name}')
                else:
                    label = element.get('label')
                
                command_key = f'button_{g}_{b}'
                group_layout.append([sg.Button(label, key=command_key)])
                commands[command_key] = element.text

        layout_tabs.append([sg.Tab(group_name, group_layout)])
                
    layout.append([sg.TabGroup(layout_tabs)])
    layout.append([sg.Button('Exit')])

    return {
        'layout': layout,
        'commands': commands,
        'config': config
    }