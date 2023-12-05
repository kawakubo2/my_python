"""Command Line Interface (CLI) for cards project."""
import os
from io import StringIO
import pathlib
import rich
from rich.table import Table
from contextlib import contextmanager
from typing import List

import netshop

import typer

app = typer.Typer(add_completion=False)


@app.command()
def version():
    """Return version of cards application"""
    print(netshop.__version__)

@app.command()
def start():
    netshop.Main.start()