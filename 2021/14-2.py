from collections import Counter
import sys
from copy import deepcopy
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day14_test.txt"
SIM_STEPS: int = 10


def make_pairings(polymer: str, pairs: dict[str, str]) -> dict[str, int]:

    resultset: dict[str, int] = {}
    for i in range(1, len(polymer)):
        if polymer[i-1: i+1] in resultset:
            resultset[polymer[i-1: i+1]] += 1
        else:
            resultset[polymer[i-1: i+1]] = 1

    for _k, _v in pairs.items():
        if _k not in resultset:
            resultset[_k] = 0

    return resultset


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

pairs: dict[str, str] = {}


for i in data[2:]:
    p = i.split('->')
    pairs[p[0].strip()] = p[1].strip()

element_counts = dict(Counter(data[0]))

polymer = make_pairings(data[0], pairs)

for step in range(SIM_STEPS):
    new_polymer = deepcopy(polymer)

    while len(polymer) > 0:
        k, v = polymer.popitem()
        if v > 0:
            new_polymer[k] = 0
            new = pairs[k]
            new_polymer[new+k[1]] += v
            new_polymer[k[0]+new] += v

            # also count the elements
            # The left and right remain, we just have to add the new one
            if new in element_counts:
                element_counts[new] += v
            else:
                element_counts[new] = v
        else:
            new_polymer[k] = 0

    polymer = new_polymer
    printDebug(f"Step {step+1}")

sorted_elements = sorted(element_counts.values())

printGood(sorted_elements[-1]-sorted_elements[0])


printOK("Time: %.5f seconds" % (timer()-start_time))
