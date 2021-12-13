import sys
from timeit import default_timer as timer
from typing import Generator, Set
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day12.txt"


def get_connections(_connections: List[List[str]], node: str) -> Generator:
    for i in _connections:
        if node != "start" and (i[0] == "start" or i[1] == "start"):
            continue

        if i[0] == node:
            yield i[1]
        if i[1] == node:
            yield i[0]


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)
connections: List[List[str]] = [a.split('-') for a in data]

# Seed starting value
paths: List[List[str]] = [["start"]]


# HERE WE GO

done = False
completed_paths: List[List[str]] = []

while not done:
    new_paths: List[List[str]] = []
    for i in paths:
        for n in get_connections(connections, i[-1]):
            if n == "end":
                completed_paths.append(i + [n])
            elif n.isupper() or (n.islower() and n not in i):
                new_paths.append(i + [n])
    if len(new_paths) == 0:
        done = True
    else:
        paths = new_paths  # and we go again

printGood(f"Number of paths: {len(completed_paths)}")
printOK("Time: %.5f seconds" % (timer()-start_time))
