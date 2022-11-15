import sys
from timeit import default_timer as timer
from os import path
import copy
from typing import Tuple
from zUtils.utils import printGood, printOK, printDisaster, printDebug

data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r", encoding='utf_8')
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    # make them individual letters
    for i in range(len(_data)):
        _data[i] = list(_data[i])  # type: ignore
    return _data


def cast(data, x, y, vector: Tuple[int, int]) -> int:
    if vector == (0, 0):
        return 0

    found = False
    cur_x = x
    cur_y = y
    while not found:
        cur_x += vector[0]
        cur_y += vector[1]
        # out of bounds
        if cur_x < 0 or cur_y < 0:
            return 0
        elif cur_x >= len(data[0]) or cur_y >= len(data):
            return 0
        elif data[cur_y][cur_x] == '#':
            return 1
        elif data[cur_y][cur_x] == 'L':
            return 0
    return 0


def check_neighbours(cur_data: list, x: int, y: int) -> int:
    total = 0
    for y_loc in range(-1, 2):
        for x_loc in range(-1, 2):
            if not (y_loc == 0 and x_loc == 0):
                total += cast(cur_data, x, y, (x_loc, y_loc))

    return total


def print_grid(d):
    output = ""
    for l in d:
        output += ' '.join(l) + "\n"
    return output


def seat_count(d):
    return print_grid(d).count('#')


def iterate(old_data):
    new_data = []
    new_data = copy.deepcopy(old_data)
    for y_loc in range(len(old_data)):
        for x_loc in range(len(old_data[y_loc])):
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if old_data[y_loc][x_loc] == 'L' and check_neighbours(old_data, x_loc, y_loc) == 0:
                new_data[y_loc][x_loc] = '#'  # type: ignore
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            if old_data[y_loc][x_loc] == '#' and check_neighbours(old_data, x_loc, y_loc) >= 5:
                new_data[y_loc][x_loc] = 'L'  # type: ignore
    printDebug(print_grid(new_data))
    return new_data


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    FILENAME = "11.txt"
else:
    FILENAME = sys.argv[1]
data = get_data(FILENAME)
if not data:
    printDisaster("NO FILE")


# HERE WE GO
# This is game of life
looping = True
loop_count = 0
while looping:
    loop_count += 1
    printOK(f"Loop {loop_count}")
    new_data = iterate(data)
    if new_data == data:
        looping = False
    else:
        data = new_data

printGood(f"Final seat count:{seat_count(data)}")
printOK(f"Time: {(timer()-start_time):.4f} seconds")
