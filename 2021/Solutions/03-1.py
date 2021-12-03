import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils.utils import *
from typing import List

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "day03.txt"


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r")
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


def pivot(data) -> List[str]:
    result: List[str] = []
    for i in range(len(data[0])):
        # for each character in the string
        # assuming all the lines are the same length
        _line: str = ""
        for _str in data:
            # grab the nth character from each line
            _line += _str[i]
        result.append(_line)
    return result


def gamma(pivot_data) -> int:
    pivot_data = pivot(data)
    result_string: str = ""
    for _l in pivot_data:
        # Now we can just to counts on the list
        result_string += '1' if _l.count('1') > _l.count('0') else '0'
    # return result in int, telling the cast function that the input is base 2
    return int(result_string, 2)


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = INPUT_FILENAME
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

# HERE WE GO
# Day 3
gamma_str: str = ""
epsilon_str: str = ""

pivot_data = pivot(data)

for _l in pivot_data:
    # Now we can just do counts on the list
    gamma_ch = '1' if _l.count('1') > _l.count('0') else '0'
    gamma_str += gamma_ch
    # epsilon is always the opposite from gamma
    epsilon_str += '1' if gamma_ch == '0' else '0'


printDebug(f"Gamma: {str(int(gamma_str,2))}")
printDebug(f"Epsilon: {str(int(epsilon_str,2))}")

printGood(f"Answer: {int(gamma_str,2) * int(epsilon_str,2)}")

printOK("Time: %.2f seconds" % (timer()-start_time))
