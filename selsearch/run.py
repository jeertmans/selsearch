from functools import partial
from typing import Any, Callable, List

import click
from pynput.keyboard import GlobalHotKeys, Listener

from .config import get_config
from .search import search_selected_text

callables: List[Callable[[], None]] = []
listeners: List[Listener] = []


def callback(f: Callable[..., Any], *args: Any, **kwargs: Any) -> Callable[[], None]:
    def wrapper() -> None:
        while listeners:
            listeners.pop().stop()

        callables.append(partial(f, *args, **kwargs))

    return wrapper


@click.command()
@click.help_option("-h", "--help")
def run() -> None:
    """
    SelSearch's main process.

    Runs until process is killed or exit shortcut is called.
    """
    config = get_config()
    urls = config.urls

    shortcuts = {}

    for shortcut, url_alias in config.shortcuts.items():
        url = urls[url_alias]
        shortcuts[shortcut] = callback(
            search_selected_text, where=url, xsel=config.xsel
        )

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
