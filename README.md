# Inkscape figure manager.

## Setup

Add the following code to the preamble of your LateX document.

```tex
\usepackage{import}
\usepackage{xifthen}
\usepackage{pdfpages}
\usepackage{transparent}

\newcommand{\incfig}[1]{%
    \def\svgwidth{\columnwidth}
    \import{./figures/}{#1.pdf_tex}
}
\pdfsuppresswarningpagegroup=1
```

This assumes the following directory structure:

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

* Watch for figures: `inkscape-figures watch`.
* Creating a figure: `inkscape-figures create 'title'`. This uses `~/.config/inkscape-figures/template.svg` as a template.
* Creating a figure in a specific folder: `inkscape-figures create 'title' path/to/figures/`.
* Select figure and edit it: `inkscape-figures edit`. This depends on `rofi`: `sudo apt install rofi`.
* Select figure in a specific and edit it: `inkscape-figures edit /path/to/figures/`.

## Vim mappings

This uses the `b:vimtex.root` variable in vim to determine the location of the figures directory.

```vim
inoremap <C-f> <Esc>: silent exec '.!inkscape-figures create "'.getline('.').'" "'.b:vimtex.root.'/figures/"'<CR><CR>:w<CR>
nnoremap <C-f> : silent exec '!inkscape-figures edit "'.b:vimtex.root.'/figures/" > /dev/null 2>&1 &'<CR><CR>:redraw!<CR>
```
