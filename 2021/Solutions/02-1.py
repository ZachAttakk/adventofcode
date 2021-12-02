import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils.utils import *
from typing import List

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "day02.txt"


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r")
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = INPUT_FILENAME
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

# HERE WE GO
# Day 2 Part 1:
# Function that processes inputs and spits out new coordinates
# Then we multiply them


def move(instruction: str) -> List[int]:
    _a, _b = instruction.split(' ')
    _command: str = _a
    _amount: int = int(_b)
    _dx: int = 0
    _dy: int = 0

    if _command == "up":
        _dy -= _amount
    elif _command == "down":
        _dy += _amount
    elif _command == "forward":
        _dx += _amount

    return [_dx, _dy]


position: List[int] = [0, 0]
for i in data:
    _delta = move(i)
    position[0] += _delta[0]
    position[1] += _delta[1]

printDebug(f"Final position: {position[0]}, {position[1]}")
printGood(position[0]*position[1])

printOK("Time: %.2f seconds" % (timer()-start_time))
