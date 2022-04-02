from dataclasses import dataclass


@dataclass
class Options:
    word: str = ""
    mean: str = ""
    new_mean: str = ""
    command: str = ""
