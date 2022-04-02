from pathlib import Path
from random import randint
from os import makedirs


class Database:
    DEFAULT_PATH = Path('~/.local/share/nwords/current_words.txt')

    def __init__(self, path: Path = DEFAULT_PATH) -> None:
        self.__connected: bool = False
        self.__path: Path = path.expanduser()

    def __parse_line(self, line: str) -> tuple[str, str]:
        delimetr_index = line.find(":")
        word = line[:delimetr_index]
        meaning = line[delimetr_index + 1:]

        return word, meaning

    def connect(self) -> bool:
        if self.__path.exists():
            self.__connected = True
        else:
            path_to_dir = "/".join(self.__path.parts[:-1])
            makedirs(path_to_dir, exist_ok=True)
            with open(self.__path, "w") as _:
                self.__connected = True
        return self.__connected

    def add(self, word: str, meaning: str) -> int:
        if self.search(word) == -1:
            with open(self.__path, "a") as db:
                db.write(f"{word}:{meaning}\n")
            return 0
        return -1

    def search(self, word: str) -> int:
        with open(self.__path, "r") as db:
            for line_num, line in enumerate(db):
                line_word, _ = self.__parse_line(line)
                if word == line_word:
                    return line_num
        return -1

    def get(self, word: str) -> tuple[str, str] | int:
        line_num = self.search(word)
        if line_num != -1:
            with open(self.__path, "r") as db:
                line = db.readlines()[line_num]
            return self.__parse_line(line)
        return -1

    def get_random(self) -> tuple[str, str] | int:
        with open(self.__path, "r") as db:
            lines = db.readlines()
            if len(lines) > 0:
                line_num = randint(0, len(lines) - 1)
                return self.__parse_line(lines[line_num])
            return -1

    def get_words(self) -> list[str]:
        with open(self.__path, 'r') as db:
            return db.readlines()

    def delete(self, word: str) -> int:
        line_num = self.search(word)
        if line_num != -1:
            with open(self.__path, "r") as db:
                lines = db.readlines()

            lines.pop(line_num)

            with open(self.__path, "w") as db:
                db.write(*lines)
            return 0
        return -1

    def change(self, word: str, new_mean: str) -> int:
        if self.delete(word) != -1:
            self.add(word, new_mean)
            return 0
        return -1
