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


def find_sum(target: int, candidates: list[int]) -> int:
    """Checks whether the sum of two candidates can possibly return the target
    """
    for a in range(len(candidates)-1):
        for b in range(a+1, len(candidates)):
            if candidates[a] + candidates[b] == target:
                return target

    return -1


def find_list(target, candidates):

    number_list = []
    for a in range(len(candidates)-1):
        number_list = [candidates[a]]
        for b in range(a+1, len(candidates)):
            number_list.append(candidates[b])
            if sum(number_list) == target:
                return number_list

    return [-1]

    # INIT
    # Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "09.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

# make the list into numbers
array = [eval(i) for i in data]
preamble_size = 25

# HERE WE GO

# find the error number
error_number = -1
for i in range(preamble_size, len(array)):
    if find_sum(array[i], array[i-preamble_size:i]) == -1:
        error_number = array[i]
        break

result_list = find_list(error_number, array)
printGood(min(result_list) + max(result_list))


printOK("Time: %.2f seconds" % (timer()-start_time))
