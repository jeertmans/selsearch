from functools import partial

import click
from pynput.keyboard import GlobalHotKeys

from .main import search_selected_text

listeners = []


def callback(f, *args, **kwargs):
    def wrapper():

        while listeners:
            listeners.pop().stop()

        callables.append(partial(f, *args, **kwargs))

    return wrapper


shortcuts = {
    "<ctrl>+<alt>+e": callback(exit),
    "<ctrl>+<alt>+m": callback(search_selected_text),
    "<ctrl>+<alt>+n": callback(search_selected_text, where="DeepL"),
    "<ctrl>+<alt>+b": callback(search_selected_text, where="WordReference"),
}

callables = []


@click.command()
def gui():
    """
    SelSearch's Graphical User Interface.

    Continuously runs in background.
    """
    while True:

        with GlobalHotKeys(shortcuts) as listener:
            listeners.append(listener)
            listener.join()

        while callables:
            f = callables.pop()
            f()
