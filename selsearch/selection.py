import os
import shutil
import keyboard
import pyperclip


class XSelNotFoundError(Exception):
    def __init__(self):
        super().__init__(
            "Executable XSel was not found. Please install XSel, see: http://www.kfish.org/software/xsel/#download."
        )


def get_selected_text_xsel():
    return os.popen("xsel").read()


def get_selected_text_alt():
    clipboard = pyperclip.paste()

    keyboard.send("ctrl+c")
    text = pyperclip.paste()

    pyperclip.copy(clipboard)
    return text


if shutil.which("xsel"):
    get_selected_text = get_selected_text_xsel
else:
    get_selected_text = get_selected_text_alt
