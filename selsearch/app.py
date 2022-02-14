import click

from .gui import gui
from .main import search_selected_text
from .where import get_list_of_search_urls


@click.group(invoke_without_command=True)
@click.option(
    "-w",
    "--where",
    type=str,
    default=None,
    help="Where to search to search for the search. Can be any value listed by `selsearch -l` or any url. Defaults to Google.",
)
@click.option(
    "-l",
    "--list-where",
    is_flag=True,
    default=False,
    help="If set, lists all the registered places to search.",
)
@click.pass_context
def cli(ctx, where, list_where):
    """
    Searches (in your default browser) the currently selected text (in any application).
    """
    if ctx.invoked_subcommand:
        return
    if list_where:
        click.echo(get_list_of_search_urls())
        return

    search_selected_text(where=where)


cli.add_command(gui)

if __name__ == "__main__":
    cli()
