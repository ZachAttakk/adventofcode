import sys
from timeit import default_timer as timer
from os import path
from typing import Tuple
from zUtils.utils import printDebug, printOK, printDisaster, printGood, printBad

data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r", encoding='utf_8')
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


def move(location: Tuple[int, int], vector: Tuple[int, int], magnitude: int) -> Tuple[int, int]:
    destination = (0, 0)
    return (location[0]+(vector[0]*magnitude), location[1]+(vector[1]*magnitude))


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    FILENAME = "12.txt"
else:
    FILENAME = sys.argv[1]
data = get_data(FILENAME)
if not data:
    printDisaster("NO FILE")

FACING_NAME = ['➡️', '⬇️', '⬅️', '⬆️']
VECTOR_ENUM = [
    (1, 0),  # E
    (0, -1),  # S
    (-1, 0),  # W
    (0, 1),  # N
]

facing = 0
location = (0, 0)

# HERE WE GO
for order in data:
    dir = order[0]
    amount = int(order[1:])
    match dir:
        case 'E':
            location = move(location, VECTOR_ENUM[0], amount)
        case 'S':
            location = move(location, VECTOR_ENUM[1], amount)
        case 'W':
            location = move(location, VECTOR_ENUM[2], amount)
        case 'N':
            location = move(location, VECTOR_ENUM[3], amount)
        case 'F':
            location = move(location, VECTOR_ENUM[facing], amount)
        case 'R':
            facing += amount // 90
            if facing > 3:
                facing = facing % 4
        case 'L':
            facing -= amount // 90
            if facing < 0:
                facing = facing % 4
    printDebug(f"{order}: {location} {FACING_NAME[facing]}")

printGood(f"Distance travelled: {abs(location[0])+abs(location[1])}")

printOK(f"Time: {(timer()-start_time):.4f} seconds")
