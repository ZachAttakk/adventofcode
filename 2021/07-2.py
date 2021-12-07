import sys
from timeit import default_timer as timer
from collections import Counter
from zUtils.utils import *
from copy import copy

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "day07.txt"


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv)


def make_crab_list(_data_line: str):

    _crabs_numbers: List[int] = list(map(int, _data_line.split(',')))
    _crabs_list: List[int] = []
    crabscounts = Counter(_crabs_numbers)
    return dict(crabscounts)


# HERE WE GO
crabscounts: dict[int, int] = make_crab_list(data[0])

lowest_fuel_target: int = -1
lowest_fuel: int = -1

max_index = max(k for k, v in crabscounts.items())
for _i in range(max_index):
    _fuel = sum(sum(range(abs(_k-_i)+1))*_v for _k, _v in crabscounts.items())
    if _fuel < lowest_fuel or lowest_fuel_target < 0:
        lowest_fuel = _fuel
        lowest_fuel_target = _i
        printDebug(f"New lowest at {lowest_fuel_target}: {lowest_fuel}")

printGood(f"Convergence at: {lowest_fuel_target}")
printGood(f"Fuel used: {lowest_fuel}")

printOK("Time: %.5f seconds" % (timer()-start_time))
