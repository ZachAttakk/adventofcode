import math
import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "08.txt"


def scenic_score(tree_list, x, y):

    value = tree_list[y][x]
    scores = []

    # to left
    count = 0
    for i in range(x-1, -1, -1):
        count += 1
        if tree_list[y][i] >= value:
            break
    scores.append(count)

    # to right
    count = 0
    for i in range(x+1, len(tree_list)):
        count += 1
        if tree_list[y][i] >= value:
            break
    scores.append(count)

    # up
    count = 0
    for i in range(y-1, -1, -1):
        count += 1
        if tree_list[i][x] >= value:
            break
    scores.append(count)

    # down
    count = 0
    for i in range(y+1, len(tree_list)):
        count += 1
        if tree_list[i][x] >= value:
            break
    scores.append(count)

    # down TODO

    return math.prod(scores)


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)
    number_grid = []
    for row in data:
        number_grid.append(list(map(int, list(row))))

    # HERE WE GO

    tree_count = []
    for row_index in range(len(number_grid)):
        for col_index in range(len(number_grid[0])):  # assuming it's square
            tree_count.append(scenic_score(number_grid, col_index, row_index))

    printGood(max(tree_count))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
