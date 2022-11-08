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
    filename = "day07.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

bag_types = {}

# HERE WE GO
# make list of bag definitions
for b in data:
    split = b.find(" bags contain ")

    bag_types[b[0:split]] = b[split+14:]

# fix latter part
for i, v in bag_types.items():
    if v == "no other bags.":
        bag_types[i] = []
        continue

    split = v.split(", ")

    new_v = []
    for x in split:
        x = x.replace(" bags", "")
        x = x.replace(" bag", "")
        x = x.replace(".", "")
        new_v.append((int(x[0]), x[2:].strip()))
    bag_types[i] = new_v


# now we check which bags can hold it

bag_set = []

new_bags = [(1, "shiny gold")]
while len(new_bags) > 0:
    found_bags = []
    for count, bag_type in new_bags:
        found_bags.extend(bag_types[bag_type]*count)

    bag_set.extend(new_bags)
    new_bags = found_bags

bag_set.extend(new_bags)

# count the bags
total = 0
for i, v in bag_set:
    total += i

printGood(total-1)
printOK("Time: %.2f seconds" % (timer()-start_time))
