import sys
from timeit import default_timer as timer
from os import path
from zUtils.utils import printOK, printDisaster, printGood, printBad

data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r", encoding='utf_8')
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    FILENAME = "advent.txt"
else:
    FILENAME = sys.argv[1]
data = get_data(FILENAME)
if not data:
    printDisaster("NO FILE")

array = []

# HERE WE GO


printOK(f"Time: {(timer()-start_time):.4f} seconds")
