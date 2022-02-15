[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/jeertmans/selsearch/main.svg)](https://results.pre-commit.ci/latest/github/jeertmans/selsearch/main)
[![Latest Release][pypi-version-badge]][pypi-version-url]
[![Python version][pypi-python-version-badge]][pypi-version-url]
# SelSearch - Internet search based on selected text

SelSearch graps text selected in any application and opens a web browser to search for.

By default, it will search on Google, but you can custimize your search to, for example, look for a DeepL translation of your text (as in the demo below).

### Installation
SelSearch can be installed using `pip`:
```
pip install selsearch
```

SelSearch best works with [XSel](http://www.kfish.org/software/xsel/), a program that grabs current selection using X. If XSel is not available on your system, SelSearch will use the clipboard to grab current selection.

### Live Demo

The demo hereunder shows how you can select text, *Linux*, in a terminal, search for it in Google. Then, search for an English to French translation of some text on DeepL.

![](https://raw.githubusercontent.com/jeertmans/selsearch/main/static/demo.gif)

### Usage

The most basic usage of SelSearch is the following:

```
selsearch
```

Optionally, you can specify the place where text is gonna be searched on:

```
selsearch -u DeepL
```

You can obtain a list of search urls with:

```
selsearch -l
```

#### Recommended Usage

However, SelSearch is best used when set as a keyboard shortcut. For example, in the demo, `selsearch` is mapped to `<ctrl>+<m>` and `selsearch -w DeepL` to `<ctrl>+<n>`. How to set up keyboard shortcuts depends on your platform.

As it may be hard to setup keyboard shortcuts on Windows, it is also possible to run the app in background with `selsearch gui`. It will continuously listen for keyboard inputs and launch appropriate commands when needed.

### Customize

SelSearch can be configured via a config file. You can generate a default one with:

```
selsearch init
```

The path will be displayed and modifications to this file will be taken into account everytime you run `selsearch` or any of its subcommands.

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
- [ ] Document how to use config file

### Contributing

Feel free to contribute or propose ideas using the [Issues](https://github.com/jeertmans/selsearch/issues) and [Pull requests](https://github.com/jeertmans/selsearch/pulls) tabs.


[pypi-version-badge]: https://img.shields.io/pypi/v/selsearch?label=SelSearch
[pypi-version-url]: https://pypi.org/project/selsearch/
[pypi-python-version-badge]: https://img.shields.io/pypi/pyversions/selsearch
[github-ci-img]: https://github.com/jeertmans/pyropey/actions/workflows/CI.yml/badge.svg
[github-ci]: https://github.com/jeertmans/pyropey/actions?query=workflow%3Aci
