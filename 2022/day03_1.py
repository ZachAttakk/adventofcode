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
    # loop strings
    for line in data:
        # split into two strings
        compartment_a = list(line[0:len(line)//2])
        compartment_b = list(line[len(line)//2:])
        # iterate through first one and find element in second.
        for item in compartment_a:
            if item in compartment_b:
                results.append(priority.index(item)+1)
                printDebug(line)
                printDebug(f"{priority.index(item)+1} ({item})")
                break

    printGood(str(sum(results)))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
