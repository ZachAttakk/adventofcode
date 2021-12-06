import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "day05.txt"


def get_coords(_input: str) -> Tuple[int, int, int, int]:
    x1 = x2 = y1 = y2 = 0

    coords: List[str] = _input.split('->')
    x1, y1 = tuple(map(int, coords[0].strip().split(',')))
    x2, y2 = tuple(map(int, coords[1].strip().split(',')))

    # Make sure the smaller number is always first
    if x1 < x2 or y1 < y2:
        return x1, y1, x2, y2
    else:
        return x2, y2, x1, y1


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv)

# HERE WE GO

# So we need a dict where the identifier is a tulpe with x,y coordinates
points: dict[Tuple[int, int], int] = {}

for _line in data:
    x1, y1, x2, y2 = get_coords(_line)
    # go through the numbers and mark them

    if not (x1 == x2 or y1 == y2):
        continue  # skip if it's not a straight line

    for _x in range(x1, x2+1):
        for _y in range(y1, y2+1):
            if (_x, _y) in points:
                points[(_x, _y)] += 1
            else:
                points[(_x, _y)] = 1

# Now we count the ones above 1
_count = 0
for _x, _y in points:
    if points[(_x, _y)] > 1:
        _count += 1

printGood(f"Count: {_count}")


printOK("Time: %.2f seconds" % (timer()-start_time))
