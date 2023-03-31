import click

from . import __version__
from .config import get_config, init
from .gui import gui
from .keys import keys
from .main import search_selected_text


@click.group(invoke_without_command=True)
@click.option(
    "-u",
    "--url",
    type=str,
    default="",
    help="Where to search on the internet. Can be any value listed by `selsearch -l` or any url. Defaults to Google.",
)
@click.option(
    "-l",
    "--list-urls",
    is_flag=True,
    default=False,
    help="If set, lists all the registered places to search.",
)
@click.version_option(__version__, "-v", "--version")
@click.help_option("-h", "--help")
@click.pass_context
def cli(ctx, url, list_urls):
    """
    Searches (in your default browser) the currently selected text (in any application).
    """
    if ctx.invoked_subcommand:
        return

    config = get_config()
    urls = config["urls"]

    if list_urls:
        max_len = max(map(len, urls.keys()))

        keys = sorted(urls.keys())

        text = "\n".join(f"{key:{max_len}s} - {urls[key]}" for key in keys)
        click.echo(text)
        return

    default_url = config["defaults"].get("url", "").lower()
    default_url = urls.get(default_url, None) or default_url

    url = urls.get(url, None) or None or default_url

    search_selected_text(where=url)


cli.add_command(init)
cli.add_command(gui)
cli.add_command(keys)

if __name__ == "__main__":
    cli()
