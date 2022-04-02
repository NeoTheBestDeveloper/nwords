from subprocess import run

from lib.Database import Database
from lib.Options import Options


class Command:

    def __init__(self, db: Database, options: Options):
        self.__db = db
        self.__options = options
        self.__set_command(options.command)

    @staticmethod
    def __show(db: Database, options: Options):
        db_result = db.get(options.word) if options.word else db.get_random()

        if db_result != -1:
            word, mean = db_result
            print(f"{word} | {mean}", end='')
        else:
            print(f"Error: no such word {options.word}")

    @staticmethod
    def __showntf(db: Database, options: Options):
        db_result = db.get(options.word) if options.word else db.get_random()

        if db_result != -1:
            word, mean = db_result
            run(f"notify-send -a neowords '{word} {mean}'", shell=True)
        else:
            print(f"Error: no such word {options.word}")

    @staticmethod
    def __showall(db: Database, options: Options):
        db_result = db.get_words()
        if db_result != -1:
            print("".join(db_result).replace(":", " - "), end='')
        else:
            print("Error: no such words")

    @staticmethod
    def __delete_word(db: Database, options: Options):
        if db.delete(options.word) == -1:
            print(f"Error: no such word {options.word}")

    @staticmethod
    def __add_word(db: Database, options: Options):
        db_result = db.add(options.word, options.mean)
        if db_result == -1:
            print("Error: word already exists")

    @staticmethod
    def __change_word(db: Database, options: Options):
        if db.change(options.word, options.new_mean) == -1:
            print(f"Error: no such word {options.word}")

    @staticmethod
    def __get_help(*args):
        doc = """
Usage:
    nw command <OPTIONS>

Commands:
    add <WORD>              - add word to current words database.
    delete <WORD>           - delete wort from current words database.
    show <WORD>             - print selected word to output with its meaning,
                              if word is void, print random word
    showntf <WORD>          - like show, but show content with nofification.
    showall                 - print all words to stdout.
    change <WORD> <NEWMEAN> - change word meaning.
    help                    - show this text.

Settings:
    NW_PATH                 - path to current words file"""

        print(doc)

    def __set_command(self, command_name: str):
        commanads_list = {
            "add": self.__add_word,
            "show": self.__show,
            "showntf": self.__showntf,
            "showall": self.__showall,
            "delete": self.__delete_word,
            "change": self.__change_word,
            "help": self.__get_help,
        }
        self.__command = commanads_list[command_name]

    def call(self):
        self.__command(self.__db, self.__options)
