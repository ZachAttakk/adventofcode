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
    filename = "day06.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

# make sure data always has a blank line at the end
if len(data[len(data)-1]) != 0:
    data.append("")

# HERE WE GO
answers = []
group = set()

for a in data:
    # blank line means process
    if len(a) == 0:
        answers.append(len(group))
        # clear group
        group = set()
    else:
        for i in a:
            group.add(i)

printGood(sum(answers))
printOK("Time: %.2f seconds" % (timer()-start_time))
