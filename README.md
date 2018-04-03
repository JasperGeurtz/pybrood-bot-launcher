# Pybrood Bot Launcher
Launcher for python scripts/bots written using [pybrood](https://github.com/neumond/pybrood)


## Usage

run `launcher.exe` while having `scriptloader.ini` in the local path or in bwapi-data/AI/

`scriptloader.ini` should contain the name of the script and the class to run
(see `example_gatherscript.py` and `scriptloader.ini` in the [github repo](https://github.com/JasperGeurtz/pybrood-bot-launcher)

it is also possible to use [droplauncher](https://github.com/adakitesystems/DropLauncher), simply move BWAPI.dll, launcher.exe, scriptloader.ini and your python script into the application.
click OK if prompted to move the other files in bwapi-data/AI.

## Building the launcher

0. `edit the launcher.py custom imports if additional python libs are needed`
1. `pip install pybrood` (if not already installed)
2. `pip install pyinstaller`
3. `pyinstaller -F launcher.py`

the `launcher.exe` should be in the `dist/` folder
