from .environ import get_environment_variable

WHERE = {
    "Google": "https://www.google.com/search?q=",
    "WordReference": "https://www.wordreference.com/enfr/",
    "DeepL": "https://www.deepl.com/translator#en/fr/",
    "GoogleScholar": "https://scholar.google.com/scholar?q=",
}


DEFAULT_SEARCH_URL = get_environment_variable("DEFAULT_SEARCH_URL")


def get_default_search_url():
    return WHERE.get(DEFAULT_SEARCH_URL, None) or DEFAULT_SEARCH_URL or WHERE["Google"]


def get_search_url(name):
    return WHERE.get(name, None) or name or get_default_search_url()


def get_list_of_search_urls():
    max_len = max(map(len, WHERE.keys()))

    keys = sorted(WHERE.keys())

    return "\n".join(f"{key:{max_len}s} - {WHERE[key]}" for key in keys)


if __name__ == "__main__":

    print(get_list_of_search_urls())
