#!/bin/python

from os import getenv
from sys import argv
from pathlib import Path

from .Database import Database
from .OptionsHandler import OptionsHandler
from .Command import Command


def main():
    # Get database.
    if db_path := getenv('NW_PATH'):
        db = Database(Path(db_path))
    else:
        db = Database()

    if not db.connect():
        print("Database is not exists")
        exit(1)

    # Get cmd options.
    opt_handler = OptionsHandler(argv)
    opt_handler.handle_options()

    options = opt_handler.get_options()
    command = Command(db, options)

    command.call()


if __name__ == "__main__":
    main()
