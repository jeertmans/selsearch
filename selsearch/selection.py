import os
import platform
import shutil
import time

import pyperclip
from pynput.keyboard import Controller, Key
from .config import get_config

keyboard = Controller()


def get_selected_text_xsel():
    return os.popen("xsel").read()


def get_selected_text_alt():
    clipboard = pyperclip.paste()

    keyboard.release(Key.alt)
    with keyboard.pressed(Key.ctrl):
        keyboard.press("c")
        time.sleep(0.1)
        keyboard.release("c")
    text = pyperclip.paste()

    pyperclip.copy(clipboard)
    return text


def get_selected_text_mac():
    clipboard = pyperclip.paste()

    keyboard.release(Key.alt)
    with keyboard.pressed(Key.cmd):
        keyboard.press("c")
        time.sleep(0.1)
        keyboard.release("c")
    text = pyperclip.paste()

    pyperclip.copy(clipboard)
    return text


config = get_config()


xsel = config["defaults"].getboolean("xsel", False)

if xsel and shutil.which("xsel"):
    get_selected_text = get_selected_text_xsel
elif platform.system() == "Darwin":
    get_selected_text = get_selected_text_mac
else:
    get_selected_text = get_selected_text_alt
