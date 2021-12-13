import sys
from timeit import default_timer as timer
from queue import SimpleQueue
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day11.txt"
SIM_STEPS: int = 100


def printGrid(text: str, _grid: List[List[int]]):
    gridprint: str = "\n".join(["".join(map(str, a)) for a in _grid])
    printOK(text+"\n"+gridprint)


def get_neighbours(_grid: List[List[int]], coord: Tuple[int, int], include_diagonals=False):

    neighbours: List[Tuple[int, int]] = []
    # because python doesn't include the last iteration in a loop
    for y in range(coord[1]-1, coord[1]+2):
        if y >= 0 and y < len(_grid):
            for x in range(coord[0]-1, coord[0]+2):
                if x >= 0 and x < len(_grid[0]) and coord != (x, y):
                    # exclude diagonals
                    if (x == coord[0] or y == coord[1]) or include_diagonals:
                        neighbours.append((x, y))
    return neighbours


def tick(_grid: List[List[int]]) -> int:

    blinks: SimpleQueue = SimpleQueue()

    blink_count: int = 0

    for y in range(len(_grid)):
        for x in range(len(_grid[0])):
            # Increase everything by 1
            _grid[y][x] += 1
            if _grid[y][x] > 9:
                blinks.put((x, y))

    while blinks.qsize() > 0:
        blink_pos = blinks.get()
        if _grid[blink_pos[1]][blink_pos[0]] > 9:
            blink_count += 1
            _grid[blink_pos[1]][blink_pos[0]] = 0
            for x, y in get_neighbours(_grid, blink_pos, True):
                if _grid[y][x] != 0:
                    _grid[y][x] += 1
                if _grid[y][x] > 9:
                    blinks.put((x, y))
    return blink_count


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

# Process data into 2D array
grid: List[List[int]] = [list(map(int, a)) for a in data]


# HERE WE GO

blinks_total: int = 0
for i in range(SIM_STEPS):
    blinks_total += tick(grid)
    # printGrid(f"Step {i+1}:", grid)

printGood(f"Total blinks: {blinks_total}")

printOK("Time: %.5f seconds" % (timer()-start_time))
