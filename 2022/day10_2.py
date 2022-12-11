import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "10.txt"


def print_screen(cycles):
    line = ""
    for cyc_index in range(len(cycles)):
        if cycles[cyc_index] >= cyc_index % 40-1 and cycles[cyc_index] <= cyc_index % 40+1:
            line += '#'
        else:
            line += '.'

        if (cyc_index+1) % 40 == 0:
            printOK(line)
            line = ""


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
    #printGood(sum([cycles[i]*(i+1) for i in range(19, len(cycles), 40)]))
    print_screen(cycles)

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
