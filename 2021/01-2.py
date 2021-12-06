import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "advent.txt"


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
# Day 1 Part 2:
# Check how many times the number gets bigger,
# when the number is made up of the last 3 numbers.


def last3(index: int) -> int:
    if index < 2:
        return -1  # sanity check
    return int(data[index]) + int(data[index-1]) + int(data[index-2])


counter: int = 0
for i in range(3, len(data)):
    # because we step back 1 in the condition,
    # we need to start high enough so the last 3 begins at 0
    if last3(i) > last3(i-1):  # gets bigger
        counter += 1

printGood(counter)
printOK("Time: %.2f seconds" % (timer()-start_time))
