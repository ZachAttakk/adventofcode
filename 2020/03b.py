from functools import reduce
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
    filename = "03a.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

# HERE WE GO

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

results = []


for slope in slopes:
    cur_x = 0
    cur_y = 0

    shift_x = slope[0]
    shift_y = slope[1]

    tree_count: int = 0

    while cur_y < len(data):
        # Check the current position
        if data[cur_y][cur_x] == '#':
            tree_count += 1

        # Advance the position
        cur_x += shift_x
        if cur_x >= len(data[0]):
            cur_x -= len(data[0])
        cur_y += shift_y

    printOK(f"{slope}: {tree_count}")
    results.append(tree_count)

    printGood(f"Trees:{reduce(lambda x, y: x*y,results)}")
printOK("Time: %.2f seconds" % (timer()-start_time))
