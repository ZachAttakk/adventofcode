import sys
from timeit import default_timer as timer
from zUtils.utils import *
from day06_1 import find_start

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "06.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # HERE WE GO
    for entry in data:
        printGood(f"{find_start(entry, 14)}: {entry}")

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
