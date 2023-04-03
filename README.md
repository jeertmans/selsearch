[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/jeertmans/selsearch/main.svg)](https://results.pre-commit.ci/latest/github/jeertmans/selsearch/main)
[![Latest Release][pypi-version-badge]][pypi-version-url]
[![Python version][pypi-python-version-badge]][pypi-version-url]
![PyPI - Downloads](https://img.shields.io/pypi/dm/selsearch)
# SelSearch - Internet search based on selected text

<p align="center">
  <img src="https://raw.githubusercontent.com/jeertmans/selsearch/main/static/logo.png" />
</p>

SelSearch grabs text selected in any application and opens a web browser to search for.

By default, it will search on Google, but you can custimize your search to, for example, look for a DeepL translation of your text (as in the demo below).

### Installation
SelSearch can be installed using `pip`:
```
pip install selsearch
```

For more infomations about installation guidelines and known issues, see [INSTALL.md](INSTALL.md).

### Live Demo

The demo hereunder shows how you can select text, *Linux*, in a terminal, search for it in Google. Then, search for an English to French translation of some text on DeepL.

![](https://raw.githubusercontent.com/jeertmans/selsearch/main/static/demo.gif)

### Usage

While SeaSearch can be used in command line, it is recommended to use its background mode via:
```
selsearch run &
```
The `&` at the end will allow SelSearch to run in background.

SelSearch will continuously listen for (customizable) keyboard shortcuts and trigger various internet researches in response. For example, in the demo, Google search is mapped to `<ctrl>+<m>` and DeepL translation to `<ctrl>+<n>`.

It is also recommended to set up `selsearch run` to launch at startup. How to do that depends on your platform and is currently not handled by this project.

### Customize

SelSearch can be configured via a config file. You can generate a default one with:

```
selsearch init
```

The path will be displayed and modifications to this file will be taken into account everytime you run `selsearch` or any of its subcommands. The file will look something like this:

```toml
xsel = true  # Whether to use or not XSel
exit_shortcut = "<ctrl>+<alt>+e"  # Exit shortcut (optional)

[urls]
# List of urls
# You can add / remove / edit any number of lines
google = "https://www.google.com/search?q="
wordreference = "https://www.wordreference.com/enfr/"
deepl = "https://www.deepl.com/translator#en/fr/"
googlescholar = "https://scholar.google.com/scholar?q="

[shortcuts]
# List of shotcuts
# You can add / remove / edit any number of lines
"<ctrl>+0" = "google"
"<ctrl>+1" = "deepl"
"<ctrl>+2" = "wordreference"

```

You can validate your keyboard shortcuts with:

```
selsearch keys
```

Other functionnalities can be listed with:

```
selsearch --help
```

### Future Features

Here are a list of future features that I would like to add to SelSearch:

- [ ] App Icon
- [ ] Installation that defaults to launch on startup
- [x] Ability to customize keyboard shortcuts
- [ ] GUI so customize app
- [x] Use of a config folder (instead of environ variable?)
- [x] Fix keyboard shortcuts on Windows (bugs...)
- [x] Document how to use config file

### Contributing

Feel free to contribute or propose ideas using the [Issues](https://github.com/jeertmans/selsearch/issues) and [Pull requests](https://github.com/jeertmans/selsearch/pulls) tabs.


[pypi-version-badge]: https://img.shields.io/pypi/v/selsearch?label=SelSearch
[pypi-version-url]: https://pypi.org/project/selsearch/
[pypi-python-version-badge]: https://img.shields.io/pypi/pyversions/selsearch
[github-ci-img]: https://github.com/jeertmans/pyropey/actions/workflows/CI.yml/badge.svg
[github-ci]: https://github.com/jeertmans/pyropey/actions?query=workflow%3Aci
