import os
from colorama import init
from colorama import Fore, Back, Style
import colorama
init()
os.system('cls' if os.name == 'nt' else 'clear')

outputDebug = False


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
        doPrint(Style.DIM + Fore.LIGHTBLACK_EX + str(text) + Fore.RESET + Style.RESET_ALL)


def doPrint(output):
    print(output)
