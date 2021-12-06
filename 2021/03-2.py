import sys
from timeit import default_timer as timer
from os import path
import copy
from zUtils.utils import *
from typing import List, Tuple

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


def pivot(_data) -> List[str]:
    result: List[str] = []
    for i in range(len(_data[0])):
        # for each character in the string
        # assuming all the lines are the same length
        _line: str = ""
        for _str in _data:
            # grab the nth character from each line
            _line += _str[i]
        result.append(_line)
    return result


def gamma_epsilon(_data) -> Tuple[str, str]:
    pivot_data = pivot(_data)
    gamma_str: str = ""
    epsilon_str: str = ""
    for _l in pivot_data:
        # Now we can just do counts on the list
        gamma_ch = '1' if _l.count('1') >= _l.count('0') else '0'
        gamma_str += gamma_ch
        # epsilon is always the opposite from gamma
        epsilon_str += '1' if gamma_ch == '0' else '0'

    return gamma_str, epsilon_str


def oxygen_co2(_data, oxygen_or_co2: int) -> str:
    """Calculate oxygen or CO2.

    Args:
        _data ([type]): Data to start with
        oxygen_or_co2 (int): 0 for oxygen, 1 for CO2

    Returns:
        str: The only remaining result, or blank string
    """
    _result_set: List[str] = copy.deepcopy(_data)  # don't want to accidentally change the original
    for _i in range(0, len(_result_set[0])):  # assume all numbers are the same length

        filter = gamma_epsilon(_result_set)[oxygen_or_co2]
        _new_data: List[str] = [i for i in _result_set if i[_i] == filter[_i]]
        # At this point we should have a single entry in our filtered data
        if len(_new_data) == 1:
            return _new_data[0]
        else:
            _result_set = _new_data

    # If we reach this point, we accidentally filtered too far
    printDisaster("Didn't find a single result!")
    return ""  # oops


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


pivot_data = pivot(data)

gamma_str, epsilon_str = gamma_epsilon(data)


printDebug(f"Gamma: {str(int(gamma_str,2))}")
printDebug(f"Epsilon: {str(int(epsilon_str,2))}")
printGood(f"Power Consumption: {int(gamma_str,2) * int(epsilon_str,2)}")


# Part 2
oxygen_str = oxygen_co2(data, 0)
printDebug(f"Oxygen: {str(int(oxygen_str,2))}")
co2_str = oxygen_co2(data, 1)
printDebug(f"CO2: {str(int(co2_str,2))}")

printGood(f"Life Support: {int(oxygen_str,2) * int(co2_str,2)}")


printOK("Time: %.2f seconds" % (timer()-start_time))
