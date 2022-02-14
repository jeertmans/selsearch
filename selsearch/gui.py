from functools import partial

import click
from pynput.keyboard import GlobalHotKeys

from .main import search_selected_text

hotkeys = {
    "<ctrl>+m": search_selected_text,
    "<ctrl>+n": partial(search_selected_text, where="DeepL"),
    "<ctrl>+b": partial(search_selected_text, where="WordReference"),
}


@click.command()
def gui():
    """
    SelSearch's Graphical User Interface.

    Continuously runs in background.
    """
    with GlobalHotKeys(hotkeys) as listener:
        listener.join()
