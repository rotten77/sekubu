from sekubu_parser import sekubu_parser
import PySimpleGUI as sg
import shlex, subprocess
import os, sys

VERSION = '0.1.0'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def sekubu():
    data = sekubu_parser('sekubu.xml')
    try:
        sg.theme(data['config']['theme'])
        sg.theme_global(data['config']['theme'])
    except:
        pass
    window = sg.Window(f'Sekubu {VERSION}', data['layout'], icon=resource_path('sekubu.ico'))

    while True:
        event, values = window.read()
        if event in data['commands']:
            args = shlex.split(data["commands"][event])
            try:
                subprocess.Popen(args, creationflags=subprocess.CREATE_NEW_CONSOLE)
            except Exception as e:
                sg.popup_error(f'Executing the command was not successful: {e}')

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()

if __name__ == "__main__":
    sekubu()