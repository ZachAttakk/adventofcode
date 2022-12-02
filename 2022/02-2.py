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
    OK not a 2D grid now, should've seen this coming.
    The shape score is index+1
    """

    playbook = ['A', 'B', 'C']

    score = 0
    for round in data:
        plays = round.split(' ')
        points = 0
        shape_index = -1
        match plays[1]:
            case 'X':  # lose
                shape_index = playbook.index(plays[0])-1
                if shape_index < 0:
                    shape_index = 2
                points = 0
            case 'Y':  # draw
                shape_index = playbook.index(plays[0])
                points = 3
            case 'Z':  # win
                shape_index = playbook.index(plays[0])+1
                if shape_index > 2:
                    shape_index = 0
                points = 6

        score += (shape_index+1) + points

    printGood(score)
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
