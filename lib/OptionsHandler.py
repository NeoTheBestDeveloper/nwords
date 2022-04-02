from lib.Options import Options


class OptionsHandler:

    def __init__(self, args: list):
        self.__args: list = args
        self.__args_len: int = len(self.__args)
        self.__no_opt_commands = ["help", "showall", "show", "showntf"]
        self.__one_opt_commands = ["show", "showntf", "delete"]
        self.__two_opt_commands = ["add", "change"]
        self.__all_commands = [
            *self.__no_opt_commands, *self.__one_opt_commands,
            *self.__two_opt_commands
        ]

    def __get_command(self) -> str:
        if self.__args_len < 2:
            return "help"

        if self.__args[1] not in self.__all_commands:
            print("Error: unknown command.")
            exit(1)

        return self.__args[1]

    def __get_word(self) -> str:
        if self.__args_len < 3:
            print("Error: no word")
            exit(1)

        return self.__args[2]

    def __get_mean(self) -> str:
        if self.__args_len < 4:
            print("Error: no second opt")
            exit(1)

        mean = self.__args[3:self.__args_len]
        return " ".join(mean)

    def handle_options(self):
        mean: str = ""
        new_mean: str = ""

        # Getting command.
        command = self.__get_command()

        # If opt in unnessery for command exit function.
        if command in self.__no_opt_commands and self.__args_len < 3:
            self.__options = Options(command=command)
            return

        # Getting word.
        word = self.__get_word()

        # Getting second opt.
        if command in self.__two_opt_commands:
            mean = new_mean = self.__get_mean()

        self.__options = Options(word=word,
                                 mean=mean,
                                 new_mean=new_mean,
                                 command=command)

    def get_options(self) -> Options:
        return self.__options
