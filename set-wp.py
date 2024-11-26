from time import sleep
import subprocess
from os import walk
from pathlib import Path

# path of the wallpapers
path: str = ""  # write path here
wallpapers: list = list()

for dir, _, files in walk(path):
    for file in files:
        file = Path(file)
        wallpapers.append(dir + str(file))


def changeWP(sec: int) -> None:
    """
    Function iterates through the wallpapers list,
    which contains the file names and absolute paths.
    it adds some few things in order to make the command work.
    Changes the background pcture and waits for sec seconds.
    args:
    sec: int the number of seconds in between each background change
    returns: None function is used for side effects
    """
    for wp in wallpapers:
        absWp: str = "file://" + wp
        subprocess.check_output(
            [
                "gsettings",
                "set",
                "org.gnome.desktop.background",
                "picture-uri-dark",
                absWp,
            ]
        )
        sleep(sec)

    return None


while True:
    changeWP(sec=8)
