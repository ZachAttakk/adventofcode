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
    filename = "01b.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

array = []

# HERE WE GO
# INSTRUCTIONS:
# Find the two entries that sum to 2020 and then multiply those two numbers together.

for _a, outer in enumerate(data):
    for _b in range(_a, len(data)):
        for _c in range(_b, len(data)):
            if int(data[_a]) + int(data[_b]) + int(data[_c]) == 2020:
                printGood(int(data[_a]) * int(data[_b]) * int(data[_c]))


printOK("Time: %.2f seconds" % (timer()-start_time))
