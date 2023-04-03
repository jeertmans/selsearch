import click
from click import Context

from . import __version__
from .config import UrlAlias, dump, get_config, init
from .keys import keys
from .run import run
from .search import search_selected_text


@click.group(invoke_without_command=True)
@click.option(
    "-u",
    "--url",
    type=str,
    default="google",
    help="Where to search on the internet. Can be any value listed by `selsearch -l` or any url.",
    show_default=True,
)
@click.option(
    "-l",
    "--list-urls",
    is_flag=True,
    default=False,
    help="If set, list all urls and exit.",
)
@click.version_option(__version__, "-v", "--version")
@click.help_option("-h", "--help")
@click.pass_context
def cli(ctx: Context, url: UrlAlias, list_urls: bool) -> None:
    """
    Searches (in your default browser) the currently selected text (in any application).
    """
    if ctx.invoked_subcommand:
        return

    config = get_config()
    urls = config.urls

    if list_urls:
        max_len = max(map(len, urls.keys()))

        keys = sorted(urls.keys())

        text = "\n".join(f"{key:{max_len}s} - {urls[key]}" for key in keys)
        click.echo(text)
        ctx.exit(0)

    url = urls.get(url, url)  # If url is not an alias, it is treated as an HttpUrl

    search_selected_text(where=url, xsel=config.xsel)


cli.add_command(dump)
cli.add_command(init)
cli.add_command(keys)
cli.add_command(run)

if __name__ == "__main__":
    cli()
