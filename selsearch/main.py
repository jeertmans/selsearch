from .search import search_text
from .selection import get_selected_text
from .where import get_list_of_search_urls, get_search_url


def search_selected_text(where=None):
    where = get_search_url(where)
    text = get_selected_text()
    search_text(where, text)
