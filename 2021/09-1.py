import sys
from timeit import default_timer as timer
from typing import Set
from zUtils.utils import *

data: List[str] = []


# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day09.txt"

THREAT_LEVEL: int = 1
RECURSION_PANIC: int = 1000


def get_neighbours(_grid: List[List[int]], coord: Tuple[int, int]):

    neighbours: List[Tuple[int, int]] = []
    # because python doesn't include the last iteration in a loop
    for y in range(coord[1]-1, coord[1]+2):
        if y >= 0 and y < len(_grid):
            for x in range(coord[0]-1, coord[0]+2):
                if x >= 0 and x < len(_grid[0]):
                    neighbours.append((x, y))
    return neighbours


def get_value(_grid: List[List[int]], coord: Tuple[int, int]) -> int:
    # sanity check
    if coord[0] < 0 or coord[0] >= len(grid[0]) or coord[1] < 0 or coord[1] >= len(grid):
        return -1

    # y on the outside
    return _grid[coord[1]][coord[0]]


def find_lowest_neighbour(_grid: List[List[int]],
                          coordinates: Tuple[int, int], level: int = 0) -> Tuple[int, int]:

    if level > RECURSION_PANIC:
        raise(RecursionError())

    cur_value: int = get_value(_grid, coordinates)

    for i in get_neighbours(_grid, coordinates):
        new_value = get_value(_grid, i)
        if new_value >= 0 and new_value < cur_value:
            return find_lowest_neighbour(_grid, i, level+1)

    # if we reach the end of the for loop and still haven't returned:
    return coordinates


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

# Process data into 2D array
grid: List[List[int]] = [list(map(int, a)) for a in data]

# HERE WE GO

lowest_locations: Set[Tuple[int, int]] = set()

# Remember y is on the outside
for y in range(len(data)):
    for x in range(len(data[y])):
        lowest_locations.add(find_lowest_neighbour(grid, (x, y)))

total = sum(get_value(grid, a)+THREAT_LEVEL for a in lowest_locations)

printGood(total)

printOK("Time: %.5f seconds" % (timer()-start_time))
