from sekubu_parser import sekubu_parser
from sekubu_config import sekubu_config
from materialpallete_colors import pallete
import dearpygui.dearpygui as dpg
from dearpygui_ext.themes import create_theme_imgui_dark, create_theme_imgui_light
import shlex, subprocess
import os, sys

VERSION = '1.2.0'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# https://github.com/hoffstadt/DearPyGui/issues/1513
def show_info(title, message):

    # guarantee these commands happen in the same frame
    with dpg.mutex():

        viewport_width = dpg.get_viewport_client_width()
        viewport_height = dpg.get_viewport_client_height()

        with dpg.window(label=title, modal=True, no_close=True) as modal_id:
            dpg.add_text(message)
            dpg.add_button(label="Ok", width=75, user_data=(modal_id, True), callback=infobox_ok)

    # guarantee these commands happen in another frame
    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])

def infobox_ok(unused1, unused2, user_data):
    dpg.delete_item(user_data[0])

def run_command(sender):
    result = next((command for command in data['layout'] if command.get('tag') == sender), None)
    try:
        args = shlex.split(result["command"])
    except Exception as e:
        show_info('Exception', f'Parsing the command was not successful: {e}')
    try:
        if result["new_console"] == True:
            subprocess.Popen(args, creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:
            process = subprocess.Popen(args, creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result["show_output"] in ['always', 'if_not_empty']:
                stdout, stderr = process.communicate()
                stdout = stdout.decode('utf-8')

                if result["show_output"] == 'if_not_empty' and len(stdout) == 0:
                    return
                show_info(f"{result['label']}:", stdout)

    except Exception as e:
        show_info('Exception', f'Executing the command was not successful: {e}')

def resize_windows(sender, app_data, user_data):
    sekubu_config('sekubu.xml', {'width': str(app_data[0]), 'height': str(app_data[1])})

def create_gui(data):

    dpg.create_context()

    theme = create_theme_imgui_dark() if data['config']['theme'] == 'dark' else create_theme_imgui_light()
    dpg.bind_theme(theme)
    
    with dpg.window(tag="sekubu_window"):
        if data['exception']!="":
            dpg.add_text(data['exception'])
        else:
            for item in data['layout']:
                if item['type'] == 'separator':
                    dpg.add_separator()
                if item['type'] == 'text':
                    dpg.add_text(item['content'])
                if item['type'] == 'button':
                    button_id = dpg.add_button(label=item['label'], tag=item['tag'], callback=run_command)
                
                    button_color_default = "default_dark" if data['config']['theme'] == 'dark' else "default_light"

                    if data['config']['color'] != "":
                        button_color_default = data['config']['color']
                    try:
                        button_color = pallete[item['color']]
                    except:
                        button_color = pallete[button_color_default]
                    
                    print(f"Button color: {button_color.background_rgb} / {button_color.darker_rgb} / {button_color.lighter_rgb} {item['label']}")
                    
                    with dpg.theme() as button_theme:
                        with dpg.theme_component(dpg.mvButton):
                            dpg.add_theme_color(dpg.mvThemeCol_Button, button_color.background_rgb)
                            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, button_color.darker_rgb)
                            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, button_color.lighter_rgb)
                            dpg.add_theme_color(dpg.mvThemeCol_Text, button_color.front_rgb)
                    dpg.bind_item_theme(button_id, button_theme)

    
    dpg.create_viewport(title=f'Sekubu {VERSION}', width=data['config']['width'], height=data['config']['height'])
    dpg.setup_dearpygui()

    dpg.set_viewport_small_icon(resource_path('sekubu.ico'))
    dpg.set_viewport_large_icon(resource_path('sekubu.ico'))

    dpg.show_viewport()
    dpg.set_primary_window("sekubu_window", True)
    dpg.set_viewport_resize_callback(resize_windows)

    dpg.start_dearpygui()

    dpg.destroy_context()

if __name__ == "__main__":
    data = sekubu_parser('sekubu.xml')
    create_gui(data)