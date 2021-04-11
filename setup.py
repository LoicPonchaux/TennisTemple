#!/usr/bin/python3


from cx_Freeze import setup, Executable
base = None
executables = [Executable("main.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
setup(
    name = "TT_Check",
    options = options,
    version = "1.0",
    description = 'Recherche Joueur',
    executables = executables
)
