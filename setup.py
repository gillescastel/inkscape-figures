import pathlib
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="inkscape-figures",
    version="1.0.4",
    description="Script for managing inkscape figures",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/gillescastel/inkscape-figures",
    author="Gilles Castel",
    author_email="gilles@castel.dev",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['inkscapefigures'],
    scripts=['bin/inkscape-figures'],
    install_requires=['inotify', 'pyperclip', 'click', 'appdirs', 'daemonize'],
    include_package_data=True
)
