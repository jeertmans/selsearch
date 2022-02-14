import urllib.parse
import webbrowser


def search_text(where, text):
    urlsafe = urllib.parse.quote(text)
    browser = webbrowser.get()
    browser.open(f"{where}{urlsafe}")
