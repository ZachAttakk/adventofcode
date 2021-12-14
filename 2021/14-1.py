from collections import Counter
import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day14.txt"
SIM_STEPS: int = 40

# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

pairs: dict[str, str] = {}

polymer: str = data[0]

for i in data[2:]:
    p = i.split('->')
    pairs[p[0].strip()] = p[1].strip()

for step in range(SIM_STEPS):
    new_polymer = polymer[0]
    for i in range(1, len(polymer)):
        if polymer[i-1:i+1] in pairs:
            new_polymer += pairs[polymer[i-1:i+1]]
            new_polymer += polymer[i]
    polymer = new_polymer
    pol_displ = polymer if len(polymer) < 20 else polymer[0:20] + "..."
    pol_displ = polymer if len(polymer) < 20 else polymer[0:20] + "..."
    printDebug(f"Step {step+1}: length {len(polymer)}: {pol_displ}")

element_counts = Counter(polymer)
sorted_elements = element_counts.most_common()
printGood(sorted_elements[0][1] - sorted_elements[-1][1])


printOK("Time: %.5f seconds" % (timer()-start_time))
