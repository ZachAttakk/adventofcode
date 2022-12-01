import sys
from timeit import default_timer as timer
from os import path
from zUtils.utils import *


data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r", encoding='utf_8')
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    FILENAME = "13.txt"
else:
    FILENAME = sys.argv[1]
data = get_data(FILENAME)
if not data:
    printDisaster("NO FILE")

depart_time = int(data[0])
busses = data[1].split(',')
for i in range(len(busses)):
    if busses[i] == 'x':
        busses[i] = '0'
busses = list(map(int, busses))
schedule = []
for i in busses:
    schedule.append(0)


# find largest index
largest_demoninator = 0
for i in busses:
    if i != 0 and i > largest_demoninator:
        largest_demoninator = i
largest_demoninator_index = busses.index(largest_demoninator)

# set the timer at the first possible hit
#start_point = 100000000000000
start_point = 103472766719749

# Let's see where's the first point after the start point
cur_time = start_point
while cur_time % (largest_demoninator) != 0:
    cur_time += 1
cur_time -= largest_demoninator_index

# HERE WE GO
found = False
while not found:
    # step through every possible next iteration
    cur_time += largest_demoninator
    found = True

    printDebug(cur_time)

    for i in range(len(busses)):
        if busses[i] != 0 and (cur_time+i) % busses[i] != 0:
            found = False
            break

printGood(cur_time)
printOK(f"Time: {(timer()-start_time):.4f} seconds")
