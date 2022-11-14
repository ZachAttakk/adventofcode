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
data.sort()

one_counts = 0
# last jump is always three
three_counts = 1

for i in range(1, len(data)):
    match data[i]-data[i-1]:
        case 1:
            one_counts += 1
        case 3:
            three_counts += 1

printOK(f"1 jolts: {one_counts}")
printOK(f"3 jolts: {three_counts}")

printGood(one_counts * three_counts)

printOK(f"Time: {(timer()-start_time):.4f} seconds")
