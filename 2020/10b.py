from statistics import variance
import sys
from timeit import default_timer as timer
from os import path
from zUtils.utils import printOK, printBad, printGood, printDisaster

data: list[int] = []

# In this case we know it's ints


def get_data(filename) -> list[int]:
    _data: list[int] = []
    if path.exists(filename):
        f = open(filename, "r", encoding='utf_8')
        if f.mode == 'r':
            _data = list(map(int, f.read().splitlines()))
            f.close()
    return _data


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    FILENAME = "10.txt"
else:
    FILENAME = sys.argv[1]
data = get_data(FILENAME)
if not data:
    printDisaster("NO FILE")

# HERE WE GO

# There's always a zero at the beginning
data.append(0)
# there's always a last adapter three up
data.append(max(data)+3)

data.sort()

variations = 1
for adapter in data:
    new = 0
    if adapter+1 in data:
        new += 1
    if adapter+2 in data:
        new += 1
    if adapter+3 in data:
        new += 1
    variations += (new-1)

printGood(variations)

printOK(f"Time: {(timer()-start_time):.4f} seconds")
