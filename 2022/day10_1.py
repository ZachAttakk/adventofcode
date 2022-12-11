import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "10.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    x = 1
    cycles = []

    # HERE WE GO

    for instruction in data:
        parts = instruction.split()
        match parts[0]:
            case 'addx':
                # takes 2 steps
                cycles.append(x)
                cycles.append(x)
                x += int(parts[1])
            case 'noop':
                cycles.append(x)

    # Calculate output
    printGood(sum([cycles[i]*(i+1) for i in range(19, len(cycles), 40)]))

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
