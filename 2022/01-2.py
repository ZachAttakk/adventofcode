import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "01.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

    sums = []

    # HERE WE GO
    current_list = []
    for i in range(len(data)):
        if data[i] != "":
            current_list.append(int(data[i]))
        if data[i] == "" or i == len(data)-1:
            sums.append(sum(current_list))
            current_list = []

    sums.sort()
    printGood(sum(sums[-3:]))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
