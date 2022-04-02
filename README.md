# Application for leaning words.

## Installation
```
$ ./install.sh
```

## Usage

```
$ python -m neowords
```

or for comfortable work you can make alias

```
alias nw="python -m neowords"
```

## Usage exampels

### Add word to list

```
$ nw add <WORD>
```

### Show word

```
$ nw show <WORD>
```

### Delete word

```
$ nw delete <WORD>
```

## Full documentaion

```
$ nw help

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
    NW_PATH                 - path to the current words file
```
