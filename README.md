# Inkscape figure manager.

A script I use to manage figures for my LaTeX documents.
More information in this [blog post](https://castel.dev/post/lecture-notes-2/).

## Requirements

You need Python >= 3.7, as well as a picker. Current supported pickers are:

* [rofi](https://github.com/davatorium/rofi) on Linux systems
* [choose](https://github.com/chipsenkbeil/choose) on MacOS

## Installation

You can install it using pip:

```
pip3 install inkscape-figures
```

This package currently works on Linux and MacOS. If you're interested in porting it to Windows, feel free to make a pull request.

## Setup

Add the following code to the preamble of your LateX document.

```tex
\usepackage{import}
\usepackage{pdfpages}
\usepackage{transparent}
\usepackage{xcolor}

\newcommand{\incfig}[2][1]{%
    \def\svgwidth{#1\columnwidth}
    \import{./figures/}{#2.pdf_tex}
}

\pdfsuppresswarningpagegroup=1
```
This defines a command `\incfig` which can be used to include Inkscape figures.
By default, `\incfig{figure-name}` make the figure as wide as the page, but it's also possible to change the width by providing an optional argument: `\incfig[0.3]{figure-name}`.

The settings above assume the following directory structure:

```
master.tex
figures/
    figure1.pdf_tex
    figure1.svg
    figure1.pdf
    figure2.pdf_tex
    figure2.svg
    figure2.pdf
```

## Usage

* Watch for figures: `inkscape-figures watch`.
* Creating a figure: `inkscape-figures create 'title'`. This uses `~/.config/inkscape-figures/template.svg` as a template.
* Creating a figure in a specific directory: `inkscape-figures create 'title' path/to/figures/`.
* Select figure and edit it: `inkscape-figures edit`.
* Select figure in a specific directory and edit it: `inkscape-figures edit path/to/figures/`.

## Vim mappings

This assumes that you use [VimTeX](https://github.com/lervag/vimtex).

```vim
inoremap <C-f> <Esc>: silent exec '.!inkscape-figures create "'.getline('.').'" "'.b:vimtex.root.'/figures/"'<CR><CR>:w<CR>
nnoremap <C-f> : silent exec '!inkscape-figures edit "'.b:vimtex.root.'/figures/" > /dev/null 2>&1 &'<CR><CR>:redraw!<CR>
```

First, run `inkscape-figures watch` in a terminal to setup the file watcher.
Now, to add a figure, type the title on a new line, and press <kbd>Ctrl+F</kbd> in insert mode.
This does the following:

1. Find the directory where figures should be saved depending on which file you're editing and where the main LaTeX file is located, using `b:vimtex.root`.
1. Check if there exists a figure with the same name. If there exists one, do nothing; if not, go on.
1. Copy the figure template to the directory containing the figures.
1. In Vim: replace the current line – the line containing figure title – with the LaTeX code for including the figure.
1. Open the newly created figure in Inkscape.
1. Set up a file watcher such that whenever the figure is saved as an svg file by pressing <kbd>Ctrl + S</kbd>, it also gets saved as pdf+LaTeX.

To edit figures, press <kbd>Ctrl+F</kbd> in command mode, and a fuzzy search selection dialog will popup allowing you to select the figure you want to edit.


## Configuration

You can change the default LaTeX template by creating `~/.config/inkscape-figures/config.py` and adding something along the lines of the following:

```python
def latex_template(name, title):
    return '\n'.join((r"\begin{figure}[ht]",
                      r"    This is a custom LaTeX template!",
                      r"    \centering",
                      rf"    \incfig[1]{{{name}}}",
                      rf"    \caption{{{title}}}",
                      rf"    \label{{fig:{name}}}",
                      r"\end{figure}"))
```
