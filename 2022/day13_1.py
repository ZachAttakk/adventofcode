import sys
from timeit import default_timer as timer

from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "13.txt"


def check_list(a, b) -> int:
    # if one is int and the other is list, convert and check
    if type(a) == int and type(b) == list:
        a = [a]
    elif type(b) == int and type(a) == list:
        b = [b]

    # if both are lists, compare each entry
    if type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            result = check_list(a[i], b[i])
            if result != 0:
                return result
        # if nothing decides, return which is shorter
        return len(a)-len(b)

    # both are ints, return which is smaller
    if type(a) == int and type(b) == int:
        return a - b

    return 0


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

    responses = []
    for i in range(0, len(data_parsed), 2):
        responses.append(check_list(data_parsed[i], data_parsed[i+1]))

    printGood(sum([i+1 if responses[i] < 0 else 0 for i in range(len(responses))]))
    # HERE WE GO
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
