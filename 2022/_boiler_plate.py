import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day09.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # HERE WE GO

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
