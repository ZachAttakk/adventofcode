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


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "advent08.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")


width = 25
height = 6

array = []
for i in range(0, len(data[0]), (width*height)):
    newline = data[0][i:i+(width*height)]
    array.append(newline)

count_zero = []
for layer in array:
    count_zero.append(layer.count('0'))

lowest_layer = count_zero.index(min(count_zero))

printGood(str(array[lowest_layer].count('1') * array[lowest_layer].count('2')))
printOK("Time: %.2f seconds" % (timer()-start_time))
