import urllib.parse
import webbrowser

from pydantic import HttpUrl

from .selection import get_selected_text


def search_text(where: HttpUrl, text: str) -> None:
    urlsafe = urllib.parse.quote(text)
    browser = webbrowser.get()
    browser.open(f"{where}{urlsafe}")


def search_selected_text(where: HttpUrl, xsel: bool) -> None:
    text = get_selected_text(xsel)
    search_text(where, text)
