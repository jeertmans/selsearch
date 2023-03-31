from functools import partial

import click
from pynput.keyboard import GlobalHotKeys

from .config import get_config
from .main import search_selected_text

listeners = []


def callback(f, *args, **kwargs):
    def wrapper():
        while listeners:
            listeners.pop().stop()

        callables.append(partial(f, *args, **kwargs))

    return wrapper


callables = []


@click.command()
def gui():
    """
    SelSearch's Graphical User Interface.

    Continuously runs in background.
    """
    config = get_config()
    urls = config["urls"]
    default_url = config["defaults"].get("url", "").lower()
    default_url = urls.get(default_url, None) or default_url

    shortcuts = {}

    for shortcut, url in config["shortcuts"].items():
        url = urls.get(url, None) or url or default_url
        shortcuts[shortcut] = callback(search_selected_text, where=url)

    exit_shortcut = config["defaults"].get("exit", None)

    if exit_shortcut:
        shortcuts[exit_shortcut] = callback(exit)

    while True:
        with GlobalHotKeys(shortcuts) as listener:
            listeners.append(listener)
            listener.join()

        while callables:
            f = callables.pop()
            f()
