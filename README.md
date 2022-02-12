[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/jeertmans/selsearch/main.svg)](https://results.pre-commit.ci/latest/github/jeertmans/selsearch/main) [![PyPI version](https://badge.fury.io/py/selsearch.svg)](https://badge.fury.io/py/selsearch)
# SelSearch - Internet search based on selected text

SelSearch graps text selected in any application and opens a web browser to search for.

By default, it will search on Google, but you can custimize your search to, for example, look for a DeepL translation of your text (as in the demo below).

### Installation
SelSearch can be installed using `pip`:
```
pip install selsearch
```

SelSearch best works with [XSel](http://www.kfish.org/software/xsel/), a program that grabs current selection using X. If XSel is not available on your system, SelSearch will use the clipboard to grab current selection. On Linux, the latter requires a sudo access.

### Live Demo

The demo hereunder shows how you can select text, *Linux*, in a terminal, search for it in Google. Then, search for an English to French translation of some text on DeepL.

![](https://github.com/jeertmans/selsearch/blob/main/static/demo.gif)

### Usage

The most basic usage of SelSearch is the following:

```
selsearch
```

Optionally, you can specify the place where text is gonna be searched on:

```
selsearch -w DeepL
```

You can obtain a list of search urls with:

```
selsearch -l
```

#### Recommended Usage

However, SelSearch is best used when set as a keyboard shortcut. For example, in the demo, `selsearch` is mapped to `<ctrl>+<m>` and `selsearch -w DeepL` to `<ctrl>-<n>`. How to set up keyboard shortcuts depends on your platform.

### Customize

Other functionnalities can be listed with:

```
selsearch --help
```

If you desire to change the default search url, or set a custom one, you can set to environment variable `SELSEARCH_DEFAULT_SEARCH_URL` to any key listed by `selsearch -l` or any url.

Example in `~/.bashrc`:

```
export SELSEARCH_DEFAULT_SEARCH_URL="https://translate.google.be/?text="
```

### Contributing

Feel free to contribute or propose ideas using the [Issues]() and [Pull Request]() tabs.
