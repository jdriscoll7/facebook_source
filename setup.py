from cx_Freeze import setup, Executable

base = None    

executables = [Executable("facebook_login_gui_to_exe.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Facebot McHidey",
    options = options,
    version = "0.69",
    description = 'This program changes all your facebook post privacy settings to "Only Me"',
    executables = executables
)
