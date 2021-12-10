from timeit import default_timer as timer
import os
from typing import List, Tuple

from colorama import init
from colorama import Fore, Back, Style
init()

outputDebug = True


def printGood(text):
    doPrint(Fore.GREEN + str(text) + Fore.RESET)


def printOK(text):
    doPrint(Fore.RESET + Style.RESET_ALL + str(text) + Fore.RESET + Style.RESET_ALL)


def printBad(text):
    doPrint(Fore.YELLOW + Style.NORMAL + str(text) + Fore.RESET + Style.RESET_ALL)


def printDisaster(text):
    doPrint(Fore.RED + Style.BRIGHT + str(text) + Fore.RESET + Style.RESET_ALL)


def printDebug(text):
    if outputDebug:
        doPrint(Fore.LIGHTBLACK_EX + str(text) + Fore.RESET + Style.RESET_ALL)


def doPrint(output):
    print(output)

### Advent of Code init stuff ###


data: list[str] = []


def get_data(filename) -> list[str]:

    printDebug(f"Getting input file: {filename}")
    _data: list[str] = []
    if os.path.exists(filename):
        f = open(filename, "r")
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


def advent_init(filename: str, args: List[str], clear_screen=True) -> List[str]:
    if clear_screen:
        os.system('cls' if os.name == 'nt' else 'clear')

    data: list[str] = []

    if len(args) >= 2:
        printDebug(f"Filename provided: {filename}")
        filename = args[1]

    data = get_data(filename)
    if (data == []):
        printDisaster("NO FILE")

    return data
