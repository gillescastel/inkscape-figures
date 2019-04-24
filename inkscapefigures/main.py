#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path
from shutil import copy
from daemonize import Daemonize
import click

import inotify.adapters
from inotify.constants import IN_CLOSE_WRITE
from .rofi import rofi
import pyperclip
from appdirs import user_config_dir


def inkscape(path):
    subprocess.Popen(['inkscape', str(path)])


def create_latex(name, title, indent=0):
    lines = [
        r"\begin{figure}[ht]",
        r"    \centering",
        rf"    \incfig{{{name}}}",
        rf"    \caption{{{title.strip()}}}",
        rf"    \label{{fig:{name}}}",
        r"\end{figure}"]

    return '\n'.join(" " * indent + line for line in lines)

user_dir = Path(user_config_dir("inkscape-figures", "Castel"))

if not user_dir.is_dir():
    user_dir.mkdir()

roots_file =  user_dir / 'roots'
template = user_dir / 'template.svg'

if not roots_file.is_file():
    roots_file.touch()

if not template.is_file():
    source = str(Path(__file__).parent / 'template.svg')
    destination = str(template)
    copy(source, destination)

def add_root(path):
    path = str(path)
    roots = get_roots()
    if path in roots:
        return None

    roots.append(path)
    roots_file.write_text('\n'.join(roots))


def get_roots():
    return [root for root in roots_file.read_text().split('\n') if root != '']


@click.group()
def cli():
    pass


@cli.command()
def watch():
    """
    Watches for figures.
    """
    daemon = Daemonize(app='inkscape-figures', pid='/tmp/inkscape-figures.pid', action=watch_daemon)
    daemon.start()
    print("Watching figures.")

def watch_daemon():
    while True:
        roots = get_roots()

        # Watch the file with contains the paths to watch
        # When this file changes, we update the watches.
        i = inotify.adapters.Inotify()
        i.add_watch(str(roots_file), mask=IN_CLOSE_WRITE)

        # Watch the actual figure directories
        print('Watching directories: ', ', '.join(get_roots()))
        for root in roots:
            try:
                i.add_watch(root, mask=IN_CLOSE_WRITE)
            except Exception:
                pass
        for event in i.event_gen(yield_nones=False):
            (_, type_names, path, filename) = event

            # If the file containing figure roots has changes, update the
            # watches
            if path == str(roots_file):
                print('Updating watches.')
                for root in roots:
                    try:
                        i.remove_watch(root)
                    except Exception:
                        pass
                # Break out of the loop, setting up new watches.
                break

            # A file has changed
            path = Path(path) / filename

            if path.suffix != '.svg':
                continue

            print('Updated', filename)

            pdf_path = path.parent / (path.stem + '.pdf')
            name = path.stem

            # Recompile the svg file
            subprocess.run([
                'inkscape',
                '--export-area-page',
                '--export-dpi', '300',
                '--export-pdf', pdf_path,
                '--export-latex', path
            ])

            # Copy the LaTeX code to include the file to the cliboard
            pyperclip.copy(create_latex(name, beautify(name)))




@cli.command()
@click.argument('title')
@click.argument(
    'root',
    default=os.getcwd(),
    type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
def create(title, root):
    """
    Creates a figure.

    First argument is the figure directory.
    Second argument is the title of the figure

    """
    file_name = title.replace(' ', '-').lower() + '.svg'
    figures = Path(root).absolute()
    if not figures.exists():
        figures.mkdir()

    figure_path = figures / file_name

    # If a file with this name already exists, append a '2'.
    if figure_path.exists():
        print(title + ' 2')
        return

    copy(str(template), str(figure_path))
    add_root(figures)
    inkscape(figure_path)

    # Print the code for including the figure to stdout.
    # Copy the indentation of the input.
    leading_spaces = len(title) - len(title.lstrip())
    print(create_latex(figure_path.stem, title, indent=leading_spaces))


def beautify(name):
    return name.replace('_', ' ').replace('-', ' ').title()


@cli.command()
@click.argument(
    'root',
    default=os.getcwd(),
    type=click.Path(exists=True, file_okay=False, dir_okay=True)
)
def edit(root):
    """
    Edits a figure.

    First argument is the figure directory.
    """

    figures = Path(root).absolute()

    # Find svg files and sort them
    files = figures.glob('*.svg')
    files = sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)

    # Open a selection dialog using rofi
    names = [beautify(f.stem) for f in files]
    _, index, selected = rofi("Select figure", names)

    if selected:
        path = files[index]
        add_root(figures)
        inkscape(path)

if __name__ == '__main__':
    cli()
