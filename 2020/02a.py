import sys
import os
from timeit import default_timer as timer
from os import path
from typing import Tuple
from zUtils.utils import *

data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r")
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


def get_minmax(_data: str) -> Tuple[int, int, str]:
    _min: str = _data[0: _data.find('-')]
    _max = _data[_data.find('-')+1:_data.find(' ')]
    _letter = _data[_data.find(' ')+1:_data.find(':')]
    return (int(_min), int(_max), _letter)


def validate(_line: str, _min: int, _max: int, _letter: str) -> bool:

    _text_to_validate = _line.split(': ')[1]
    _count = _text_to_validate.count(_letter)
    if _min <= _count <= _max:
        return True
    else:
        return False


    # INIT
    # Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "advent.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

array = []

# HERE WE GO

count = 0

for _line in data:
    # get details
    _min, _max, _letter = get_minmax(_line)
    # validate
    valid: bool = validate(_line, _min, _max, _letter)
    if valid:
        printGood(_line)
        count += 1
    else:
        printBad(_line)

printOK(f"final count invalidates: {count}")

# Just because it's interesting to see how long things take to run...
printOK("Time: %.2f seconds" % (timer()-start_time))
