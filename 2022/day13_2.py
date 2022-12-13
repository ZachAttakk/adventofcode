import sys
from timeit import default_timer as timer

from day13_1 import check_list
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "13.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    data_parsed = []
    for line in data:
        # assuming there will always be pairs so we don't need the blank lines
        if line == "":
            continue
        data_parsed.append(eval(line))

    # also add divider packets
    data_parsed.append([[2]])
    data_parsed.append([[6]])
    # HERE WE GO

    sorted = False
    while not sorted:
        sorted = True
        for i in range(1, len(data_parsed)):
            if check_list(data_parsed[i-1], data_parsed[i]) > 0:
                sorted = False
                data_parsed.insert(i-1, data_parsed.pop(i))
                break

    printGood((data_parsed.index([[2]])+1)*(data_parsed.index([[6]])+1))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
