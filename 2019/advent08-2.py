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

# 0 black
# 1 white
# 2 transparent

array = []
for i in range(0, len(data[0]), (width*height)):
    newline = data[0][i:i+(width*height)]
    array.append(newline)

final_image = [2]*width*height
for layer in array:
    for i in range(len(layer)):
        if layer[i] != '2' and final_image[i] == 2:
            final_image[i] = int(layer[i])

printout = ""
for i in range(len(final_image)):
    newline = ""
    if final_image[i] == 0:
        newline = Back.BLACK + " "
    elif final_image[i] == 1:
        newline = Back.WHITE + " "

    if i != 0 and (i+1) % width == 0:
        newline = newline + Style.RESET_ALL + "\n"

    printout = printout + newline

print(printout + Style.RESET_ALL)

printOK("Time: %.2f seconds" % (timer()-start_time))
