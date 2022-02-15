from appdirs import user_config_dir
import os
import configparser

import click
from appdirs import user_data_dir

DEFAULT_CONFIG = {
    "defaults": {
        "exit": "<ctrl>+<alt>+e",
        "url": "google",
    },
    "urls": {
        "google": "https://www.google.com/search?q=",
        "wordreference": "https://www.wordreference.com/enfr/",
        "deepl": "https://www.deepl.com/translator#en/fr/",
        "googlescholar": "https://scholar.google.com/scholar?q=",
    },
    "shortcuts": {
        "<ctrl>+<alt>+m": "google",
        "<ctrl>+<alt>+n": "deepl",
        "<ctrl>+<alt>+b": "wordreference",
    },
}


default_config = configparser.ConfigParser()
default_config.read_dict(DEFAULT_CONFIG)


def get_config_dir():
    return user_config_dir("selsearch", "jeertmans")


def get_config_file(config_dir):
    return os.path.join(config_dir, "selsearch.ini")


def get_config():
    config_file = get_config_file(get_config_dir())

    if os.path.exists(config_file):
        config = configparser.ConfigParser()
        with open(config_file, "r") as f:
            config.read_file(f)
        return config
    else:
        return default_config


@click.command()
@click.option(
    "--force",
    is_flag=True,
    default=False,
    help="If set, overwrite any existing config file.",
)
def init(force):
    """
    Initialize config file and return its path.
    """
    config_dir = get_config_dir()
    config_file = get_config_file(config_dir)

    if not force and os.path.exists(config_file):
        raise click.UsageError(
            f"Config file `{config_file}` already exists. To overwrite it, use `--force` option."
        )

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    with open(config_file, "w") as f:
        default_config.write(f)

    click.secho(f"Successfully created config file `{config_file}`.", fg="green")
