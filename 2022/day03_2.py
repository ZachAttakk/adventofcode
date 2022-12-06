import sys
from timeit import default_timer as timer
from zUtils.utils import *
from string import ascii_lowercase, ascii_uppercase

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "03.txt"


""" 
Priority starts at 1, all lowercase, then uppercase. So I can make a lookup list and +1 the index
 """

priority = list(ascii_lowercase + ascii_uppercase)


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)
    # list of results
    results = []
    # HERE WE GO
    # loop strings in threes
    for group_index in range(0, len(data), 3):
        # match three strings, then find the common element between them
        # Use the first line as the iterator
        elf_1 = list(data[group_index])
        elf_2 = list(data[group_index+1])
        elf_3 = list(data[group_index+2])
        for t in elf_1:
            if t in elf_2 and t in elf_3:
                results.append(priority.index(t)+1)
                printDebug(f"{priority.index(t)+1} ({t})")
                break

    printGood(str(sum(results)))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
