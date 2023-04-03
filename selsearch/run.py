from functools import partial

import click
from pynput.keyboard import GlobalHotKeys

from .config import get_config
from .search import search_selected_text

listeners = []


def callback(f, *args, **kwargs):
    def wrapper():
        while listeners:
            listeners.pop().stop()

        callables.append(partial(f, *args, **kwargs))

    return wrapper


callables = []


@click.command()
@click.help_option("-h", "--help")
def run():
    """
    SelSearch's main process.

    Runs until process is killed or exit shortcut is called.
    """
    config = get_config()
    urls = config.urls

    shortcuts = {}

    for shortcut, url_alias in config.shortcuts.items():
        url = urls[url_alias]
        shortcuts[shortcut] = callback(search_selected_text, where=url, xsel=config.xsel)

    exit_shortcut = config.exit_shortcut

    if exit_shortcut:
        shortcuts[exit_shortcut] = callback(exit)

    while True:
        with GlobalHotKeys(shortcuts) as listener:
            listeners.append(listener)
            listener.join()

        while callables:
            f = callables.pop()
            f()
