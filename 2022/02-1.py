import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "02.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv)

    # HERE WE GO

    """
    Rock: A, X
    Paper: B, Y
    Scissors: C, Z

    This is a 2D grid
    """
    results = {
        'A': {
            'X': 3,
            'Y': 6,
            'Z': 0
        },
        'B': {
            'X': 0,
            'Y': 3,
            'Z': 6
        },
        'C': {
            'X': 6,
            'Y': 0,
            'Z': 3
        }
    }

    shape = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    score = 0
    for round in data:
        plays = round.split(' ')
        result = results[plays[0]][plays[1]] + shape[plays[1]]
        printDebug(f"{round}: {result}, {score+result}")
        score += result

    printGood(score)
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
