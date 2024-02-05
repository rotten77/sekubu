def create_example_config(file_path: str):
    CONFIG = '''<?xml version="1.0" encoding="UTF-8"?>
<sekubu theme="DefaultNoMoreNagging">
    <group>
        <name>Configuration</name>
        <text>Configuration file not found.</text>
        <separator />
        <text>Edit "sekubu.xml" and restart the application.</text>
    </group>

    <group>
        <name>Examples</name>
        <button label="Calculator">calc.exe</button>
        <button label="Computer name">powershell.exe -NoExit -Command "$env:COMPUTERNAME"</button>
    </group>
</sekubu>'''
    with open(file_path, 'w') as f:
        f.write(CONFIG)