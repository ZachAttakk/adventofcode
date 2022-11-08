import sys
import os
from timeit import default_timer as timer
from os import path
from zUtils.utils import *

data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r")
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


def parseseat(part) -> int:

    # get groups
    row = part[:7]
    seat = part[7:]

    # set starting value
    row_start = 0
    row_end = 127
    seat_start = 0
    seat_end = 7

    for i in row:
        gap = row_end-row_start+1
        match i:
            case 'F':
                row_end -= gap//2
            case 'B':
                row_start += gap//2

    for i in seat:
        gap = seat_end-seat_start+1
        match i:
            case 'L':
                seat_end -= gap//2
            case 'R':
                seat_start += gap//2

    # the end result should always be the same

    return 8 * row_end + seat_end


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "05.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

array = []

# HERE WE GO

for l in data:
    seat = parseseat(l)
    printOK(l + ": " + str(seat))
    array.append(seat)

printGood(max(array))
printOK("Time: %.2f seconds" % (timer()-start_time))
