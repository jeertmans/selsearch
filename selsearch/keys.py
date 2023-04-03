from typing import Dict, Optional, Union

import click
from pynput.keyboard import Key, KeyCode, Listener

EventType = Optional[Union[Key, KeyCode]]
events: Dict[EventType, None] = dict()


def key_repr(key: EventType) -> str:
    key = str(key)
    if "Key." in key:
        return f"<{key[4:]}>"
    else:
        return key[1]


def on_press(event: EventType) -> bool:
    if event == Key.esc:
        click.echo("Pressed <esc>, now leaving.")
        return False
    else:
        events[event] = None
        text = "+".join(map(key_repr, events.keys()))
        click.echo(f"Pressed {text}")
        return True


def on_release(event: EventType) -> None:
    events.pop(event, None)


@click.command()
@click.help_option("-h", "--help")
def keys() -> None:
    """
    Print keys as they are pressed.

    This is especially usefull to validate your shortcuts.
    """
    click.echo(
        "From now one, key presses are shown down below and their effects are suppressed.\nPress <esc> to exit."
    )

    with Listener(on_press=on_press, on_release=on_release, suppress=True) as listener:
        listener.join()
