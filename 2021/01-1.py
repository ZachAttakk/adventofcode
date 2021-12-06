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
# Day 1 Part 1: check how many times the number gets bigger
counter: int = 0
for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]):  # gets bigger
        counter += 1

printGood(counter)
printOK("Time: %.2f seconds" % (timer()-start_time))
