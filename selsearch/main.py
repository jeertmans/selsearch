from .search import search_text
from .selection import get_selected_text


def search_selected_text(where=None):
    text = get_selected_text()
    search_text(where, text)
