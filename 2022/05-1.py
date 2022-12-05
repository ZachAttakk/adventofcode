import copy
import sys
from timeit import default_timer as timer

import regex
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "05.txt"

"""
    Blank line for when the instructions start.
    Then regex for instructions and slice results.
    Best probably to write a function for it
"""


instructions_regex = regex.compile(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)")


def shift(old_list: list[list[str]], number: int, start_index: int, end_index: int) -> list[list[str]]:
    """Returns a new list with the number of cells moved from one position to another.

    Args:
        old_list (list[str]): Original data
        number (int): Number of entries to move
        start_index (int): From where
        end_index (int): To where

    Returns:
        list[str]: New list with changes applied
    """
    results: list[list[str]] = copy.deepcopy(old_list)

    # Indexes start at one
    start_index -= 1
    end_index -= 1
    for i in range(number):
        results[end_index].insert(0, results[start_index].pop(0))

    return results


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # get assignments block
    instruction_start_index = data.index("")
    crate_data_raw = data[: instruction_start_index-1]
    # list for crate columns
    crate_columns = []
    # rearrange data to usable format
    # so for each column index...
    for column_index in range(1, len(crate_data_raw[len(crate_data_raw)-1]), 4):
        new_crate_col = []
        # ... iterate vertically...
        for line_index in range(len(crate_data_raw)):
            # ... and index the letters
            crate = crate_data_raw[line_index][column_index]
            if not crate.isspace():
                new_crate_col.append(crate_data_raw[line_index][column_index])
        crate_columns.append(new_crate_col)

    # follow instructions

    instructions = [list(map(int, instructions_regex.match(i).groups()))
                    for i in data[instruction_start_index+1:]]

    # HERE WE GO
    for i in instructions:
        crate_columns = shift(crate_columns, *i)

    topstack = "".join([a[0] for a in crate_columns])
    printGood(topstack)
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
