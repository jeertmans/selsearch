import os
from pathlib import Path
from typing import Any, Dict, Optional

import click
import rtoml as toml
from appdirs import user_config_dir
from pydantic import BaseModel, HttpUrl, root_validator

Shortcut = str
UrlAlias = str


class Config(BaseModel):  # type: ignore
    xsel: bool = True
    exit_shortcut: Optional[Shortcut] = "<ctrl>+<alt>+e"
    urls: Dict[UrlAlias, HttpUrl] = {
        "google": "https://www.google.com/search?q=",
        "wordreference": "https://www.wordreference.com/enfr/",
        "deepl": "https://www.deepl.com/translator#en/fr/",
        "googlescholar": "https://scholar.google.com/scholar?q=",
    }
    shortcuts: Dict[Shortcut, UrlAlias] = {
        "<ctrl>+0": "google",
        "<ctrl>+1": "deepl",
        "<ctrl>+2": "wordreference",
    }

    @root_validator
    def validate_urls(cls, values: Dict[Any, Any]) -> Dict[Any, Any]:
        urls: Dict[UrlAlias, HttpUrl] = values.get("urls")  # type: ignore
        shortcuts: Dict[Shortcut, UrlAlias] = values.get("shortcuts")  # type: ignore

        for shortcut, url_alias in shortcuts.items():
            if url_alias not in urls:
                raise ValueError(
                    "An error occured while parsing [shortcuts]: "
                    f"`{url_alias}` (shortcut: `{shortcut}`) "
                    "does not have an entry in [urls], please"
                    " create one!"
                )

        return values

    @classmethod
    def parse_toml(cls, file: Path) -> "Config":
        return cls.parse_obj(toml.loads(file.read_text()))  # type: ignore


def get_config_dir() -> Path:
    return Path(user_config_dir("selsearch", "jeertmans"))


def get_config_file(config_dir: Path) -> Path:
    if config_dir.joinpath("selsearch.ini").exists():
        import warnings

        warnings.warn(
            "It seems that you have an old `selsearch.ini` "
            f"file located in `{config_dir}`, but selsearch now uses "
            "`selsearch.toml` config file. Please delete the `.ini`"
            "file to suppress this warning."
        )
    return config_dir.joinpath("selsearch.toml")


def get_config() -> Config:
    config_file = get_config_file(get_config_dir())

    if os.path.exists(config_file):
        return Config.parse_toml(config_file)
    else:
        return Config()


@click.command()
@click.option(
    "--force",
    is_flag=True,
    default=False,
    help="If set, overwrite any existing config file.",
)
@click.help_option("-h", "--help")
def init(force: bool) -> None:
    """
    Initialize config file and return its path.
    """
    config_dir = get_config_dir()
    config_file = get_config_file(config_dir)

    if not force and config_file.exists():
        raise click.UsageError(
            f"Config file `{str(config_file)}` already exists. To overwrite it, use `--force` option."
        )

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    toml.dump(Config().dict(), config_file)

    click.secho(f"Successfully created config file `{str(config_file)}`.", fg="green")


@click.command()
@click.help_option("-h", "--help")
def dump() -> None:
    """
    Dump the config file to stdout.
    """
    config = get_config().dict()

    urls = config["urls"]

    for url_alias, url in urls.items():
        urls[url_alias] = str(url)

    click.echo(toml.dumps(config))
