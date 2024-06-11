def create_example_config(file_path: str):
    CONFIG = '''<?xml version="1.0" encoding="UTF-8"?>
<sekubu theme="dark" width="250" height="250">
    <text>This is an example</text>
    <separator/>
    <button label="Calculator">calc.exe</button>
    <button label="Computer name" new_console="false" show_output="always">powershell.exe -Command "$env:COMPUTERNAME"</button>
    <separator/>
    <text>What to do?</text>
    <text>1) Close application</text>
    <text>2) Edit "sekubu.xml"</text>
    <text>3) Start application</text>
</sekubu>'''
    with open(file_path, 'w') as f:
        f.write(CONFIG)