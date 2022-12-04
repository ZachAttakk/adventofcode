import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "04.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # HERE WE GO
    fully_inclusive_count = 0
    for line in data:
        # create two elves
        elves = line.split(',')
        # breaks the two elves into lists
        elves_numbers = []
        for elf_index in range(len(elves)):
            elves_numbers.append(list(map(int, elves[elf_index].split('-'))))

        # check whether elves_numbers[0] is inside elves_numbers[1]
        if elves_numbers[0][0] >= elves_numbers[1][0] and elves_numbers[0][1] <= elves_numbers[1][1]:
            printOK(f"{elves_numbers[0]} is inside {elves_numbers[1]}")
            fully_inclusive_count += 1
        # check whether elves_numbers[1] is inside elves_numbers[0]
        elif elves_numbers[1][0] >= elves_numbers[0][0] and elves_numbers[1][1] <= elves_numbers[0][1]:
            printOK(f"{elves_numbers[1]} is inside {elves_numbers[0]}")
            fully_inclusive_count += 1
        else:
            printDebug(f"{elves_numbers[0]} and {elves_numbers[1]} are not inclusive")

    printGood(f"Total amount of includes: {fully_inclusive_count}")
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
