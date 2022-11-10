import string
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


def process(group) -> int:

    all_answers = set(string.ascii_lowercase)

    for ans in group:
        # for each answer
        new_ans = set()
        # we check all the letters
        for i in all_answers:
            if i in ans:
                # if the letter still exists, keep it
                new_ans.add(i)
        # set the kept letters are the remainder
        all_answers = new_ans

    return len(all_answers)


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
group = []

for a in data:
    # blank line means process
    if len(a) == 0:
        answers.append(process(group))
        # clear group
        group = []
    else:
        group.append(a)

printGood(sum(answers))
printOK("Time: %.2f seconds" % (timer()-start_time))
