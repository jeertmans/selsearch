import click
import webbrowser
import urllib.parse
from .where import get_list_of_search_urls, get_search_url
from .selection import get_selected_text


def search_selected_text(where):
    text = get_selected_text()
    urlsafe = urllib.parse.quote_plus(text)
    browser = webbrowser.get()
    browser.open(f"{where}{urlsafe}")


@click.command()
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
def main(where, list_where):
    """
    Searches (in your default browser) the currently selected text (in any application).
    """
    if list_where:
        click.echo(get_list_of_search_urls())
        return

    where = get_search_url(where)
    text = get_selected_text()
    urlsafe = urllib.parse.quote(text)
    browser = webbrowser.get()
    browser.open(f"{where}{urlsafe}")


if __name__ == "__main__":
    main()
