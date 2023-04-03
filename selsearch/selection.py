import os
import platform
import shutil
import time

import pyperclip
from pynput.keyboard import Controller, Key

XSEL_AVAILABLE = shutil.which("xsel") is not None
MACOS = platform.system() == "Darwin"
keyboard = Controller()


def get_selected_text_xsel() -> str:
    return os.popen("xsel").read()


def get_selected_text_alt() -> str:
    clipboard = pyperclip.paste()

    keyboard.release(Key.alt)
    with keyboard.pressed(Key.ctrl):
        keyboard.press("c")
        time.sleep(0.1)
        keyboard.release("c")
        time.sleep(0.1)
    text = pyperclip.paste()

    pyperclip.copy(clipboard)
    return text  # type: ignore


def get_selected_text_mac() -> str:
    clipboard = pyperclip.paste()

    keyboard.release(Key.alt)
    with keyboard.pressed(Key.cmd):
        keyboard.press("c")
        time.sleep(0.1)
        keyboard.release("c")
        time.sleep(0.1)
    text = pyperclip.paste()

    pyperclip.copy(clipboard)
    return text  # type: ignore


def get_selected_text(xsel: bool) -> str:
    if xsel and XSEL_AVAILABLE:
        return get_selected_text_xsel()
    elif MACOS:
        return get_selected_text_mac()
    else:
        return get_selected_text_alt()
