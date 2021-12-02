import sys
import os
from timeit import default_timer as timer
from os import path
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


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "01a.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

array = []

# HERE WE GO
# INSTRUCTIONS:
# Find the two entries that sum to 2020 and then multiply those two numbers together.

for _o, outer in enumerate(data):
    for _i in range(_o, len(data)):
        if int(data[_o]) + int(data[_i]) == 2020:
            printGood(int(data[_o]) * int(data[_i]))


printOK("Time: %.2f seconds" % (timer()-start_time))
