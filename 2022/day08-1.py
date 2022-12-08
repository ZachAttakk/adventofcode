import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "08.txt"


def visible(tree_list, x, y):
    # sanity checks
    if x == 0 or x == len(tree_list[0])-1:  # assuming square
        return True
    if y == 0 or y == len(tree_list)-1:
        return True

    value = tree_list[y][x]

    # from left
    if all(t < value for t in tree_list[y][0:x]):
        return True
    # from right
    if all(t < value for t in tree_list[y][x+1:]):
        return True

    # list comprehension for vertical
    column = list([tree_list[t][x] for t in range(len(tree_list))])
    # from top
    if all(t < value for t in column[0:y]):
        return True
    # from bottom
    if all(t < value for t in column[y+1:]):
        return True

    return False


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
            tree_count.append(visible(number_grid, col_index, row_index))

    printGood(sum(tree_count))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
