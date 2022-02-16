import click
from pynput.keyboard import Listener, Key


events = dict()


def key_repr(key):
    key = str(key)
    if "Key." in key:
        return f"<{key[4:]}>"
    else:
        return key[1]


def on_press(event):
    if event == Key.esc:
        click.echo("Pressed <esc>, now leaving.")
        return False
    else:
        events[event] = None
        text = "+".join(map(key_repr, events.keys()))
        click.echo(f"Pressed {text}")


def on_release(event):
    events.pop(event, None)


@click.command()
def keys():
    """
    Enters a key listening mode where every key input is printed in the terminal.

    This is especially usefull to validate your shortcuts.
    """
    click.echo(
        "From now one, key presses are shown down below and their effects are suppressed.\nPress <esc> to exit."
    )

    with Listener(on_press=on_press, on_release=on_release, suppress=True) as listener:
        listener.join()
