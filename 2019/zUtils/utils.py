from colorama import init
from colorama import Fore, Back, Style
init()

outputDebug = True

def printGood(text):
  doPrint(Fore.GREEN + text + Fore.RESET)
  
def printOK(text):
  doPrint(Fore.RESET + Style.RESET_ALL + text + Fore.RESET + Style.RESET_ALL)
  
def printBad(text):
  doPrint(Fore.YELLOW + Style.NORMAL + text + Fore.RESET + Style.RESET_ALL)
  
def printDisaster(text):
  doPrint(Fore.RED + Style.BRIGHT + text + Fore.RESET + Style.RESET_ALL)

def printDebug(text):
  if outputDebug: doPrint(Style.DIM + Fore.LIGHTBLACK_EX + text + Fore.RESET + Style.RESET_ALL)

def doPrint(output):
  print(output)
  