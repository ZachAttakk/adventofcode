import sys
import os
from timeit import default_timer as timer
from os import path

from sympy import false, true
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

# Required fields
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)


requirements = [
    "byr:",
    "iyr:",
    "eyr:",
    "hgt:",
    "hcl:",
    "ecl:",
    "pid:"
]


def validate(psp: str) -> str:
    for req in requirements:
        if req not in psp:
            return req

    return ""


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "04a.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")

array = []

total_count = 0

# HERE WE GO
passport = ""
for i in data:
    # first concatenate all entries from a single passport, then process
    if len(i) == 0:  # blank line means process
        error = validate(passport)
        if error == "":
            printGood(passport)
            total_count += 1
        else:
            printBad(passport + ": missing " + str(error))
        passport = ""
    else:
        passport = passport + " " + i

printOK(f"Total: {total_count:d}")
printOK("Time: %.2f seconds" % (timer()-start_time))
