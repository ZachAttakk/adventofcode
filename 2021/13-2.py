import sys
from timeit import default_timer as timer
from typing import Set
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day13.txt"


def printGrid(text: str, page: Set[Tuple[int, int]], width: int, height: int):
    grid = []
    for y in range(height):
        _line = []
        for x in range(width):
            _line.append('.')
        grid.append(_line)

    for i in page:
        x, y = i
        grid[y][x] = '#'
    gridprint: str = "\n".join(["".join(a) for a in grid])
    printOK(text+"\n"+gridprint)


def fold(page: Set[Tuple[int, int]], *, fold_x: int = 0, fold_y: int = 0) -> Set[Tuple[int, int]]:
    new_page: Set[Tuple[int, int]] = set()

    for dot in page:
        new_x = fold_x-(dot[0]-fold_x) if fold_x > 0 and dot[0] > fold_x else dot[0]
        new_y = fold_y-(dot[1]-fold_y) if fold_y > 0 and dot[1] > fold_y else dot[1]
        new_page.add((new_x, new_y))

    return new_page


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

# Make the paper and the instructions
page: Set[Tuple[int, int]] = set()
instructions: List[str] = []

for line in data:
    if line.startswith("fold along"):
        instructions.append(line)
    elif line.find(',') >= 0:
        values = line.split(',')
        page.add((int(values[0]), int(values[1])))

for inst in instructions:
    printOK(f"Number of dots: {len(page)}")
    printDebug(inst+"...")
    if inst.find("x", 11) >= 0:
        page = fold(page, fold_x=int(inst.split('=')[1]))
    else:
        page = fold(page, fold_y=int(inst.split('=')[1]))

printGrid("State: ", page, 40, 6)
printGood(f"Number of dots: {len(page)}")

printOK("Time: %.5f seconds" % (timer()-start_time))
