import sys
import os
from timeit import default_timer as timer
from os import path

import regex
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
    filename = "day07.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

bag_types = []

# HERE WE GO
# make list of bag definitions
for b in data:
    split = b.find(" bags contain ")

    bag_types.append((b[0:split], b[split+14:]))

# now we check which bags can hold it

bag_combinations = set()
bag_combinations.add("shiny gold")

new_bags = set()
new_bags.add("shiny gold")  # dummy to get it rolling

old_count = len(bag_combinations)
new_count = 100000

while old_count != new_count:
    old_count = len(bag_combinations)
    new_bags = set()
    for b in bag_combinations:
        for i, v in bag_types:
            if b in v:
                new_bags.add(i)
    bag_combinations.update(new_bags)
    new_count = len(bag_combinations)

printGood(len(bag_combinations)-1)
printOK("Time: %.2f seconds" % (timer()-start_time))
