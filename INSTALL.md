# Installing SelSearch

This document provides platform specific installation guidelines.

- [All-Plaftorms](#all-platforms)
- [Linux](#linux)
- [MacOS](#macos)
- [Windows](#windows)

# All Platforms

## Requirements

SelSearch requires Python>=3.6 to be installed.

Several Python packages are also required, but automatically installed with `pip`:
- [appdirs](https://github.com/ActiveState/appdirs) for determining best path for config folder
- [Click](https://click.palletsprojects.com/en/8.0.x/) for creating the command line interface
- [pynput](https://pynput.readthedocs.io/en/latest/#) for controlling and motoring the beyboard
- [Pyperclip](https://pyperclip.readthedocs.io/en/latest/) for copying and pasting text to the clipboard

## PIP Install

In a terminal / anaconda prompt, latest version of SelSearch can be obtained via pip:

```
pip install selsearch
```

Verify your installation with `selsearch -v`.

Optionally, you can generate a config file with:

```
selsearch init
```

# Linux

## (Optional) Install XSel

As most Linux distrubutions use X, it is recommended to install [XSel](http://www.kfish.org/software/xsel/#download) as it provides the best experience.

# MacOS

## (Optional) Install XSel

As MacOS distrubutions (can) use X, it is recommended to install [XSel](https://formulae.brew.sh/formula/xsel) as it provides the best experience.

## Known Issues

*Many thanks to [mmakdis](https://github.com/mmakdis) for providing help and screenshots for the MacOS version.*

### * `This process is not trusted! [...]`

You need to allow your terminal to use your keyboard.

First, open *System Preferences*, and search for *Security & Privacy*.

<p align="center">
  <img src="static/macos/not-trusted-1.png" alt="drawing" height="600"/>
</p>

Then, in *Accessibility*, allow the *Terminal* application to control your computer.

<p align="center">
  <img src="static/macos/not-trusted-2.png" alt="drawing" height="600"/>
</p>

Repeat the same process for *Input Monitoring*.

<p align="center">
  <img src="static/macos/not-trusted-3.png" alt="drawing" height="600"/>
</p>

### * `xsel: Can't open display: (null): Inappropriate ioctl for device`

In a terminal, or in your `.bashrc` (or equivalent), write `export DISPLAY=:1`.
Verify that it works by testing the command `xsel`.

If this does fix the problem, disable XSel in the config file and open an [issue](https://github.com/jeertmans/selsearch/issues).

### * My shortcut using `<alt>` doest not work

It seems that the `<alt>` key is mapped to `<option>` on MacOS keyboards.

# Windows

## Known Issues

### * `'selsearch' is not recognized as an internal or external command [...]`

Most probably, when you installed SelSearch, a warning told you that `Path\To\Python\Scripts\` was not in `PATH`.
This means that the `selsearch` command is not directly exposed to you in the terminal.

To solve this, you must add the path to Python's scripts folder in the environment variable `PATH`. See this [tutorial](https://datatofish.com/add-python-to-windows-path/) for more details.
