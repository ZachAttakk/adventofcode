import sys
import os
from timeit import default_timer as timer
from os import path
import re

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
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


requirements = [
    "byr:",
    "iyr:",
    "eyr:",
    "hgt:",
    "hcl:",
    "ecl:",
    "pid:"
]

eye_colors = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
]

# regex

regex_hcl = re.compile("#[0-9|a-f]{6}")
regex_pid = re.compile("[0-9]{9}")


def validate(psp: str) -> str:
    psp_v = psp.split(" ")
    # first check that they all exist
    for req in requirements:
        if psp.count(req) != 1:
            return req + " not exactly 1 instance"

        # then check each parameter
        for p in psp_v:
            if p.strip().startswith(req):
                if not check(p.strip()):
                    return req + " invalid"
                break

    return ""


def check(p: str) -> bool:
    p_item = p.split(':')
    match p_item[0]:
        case "byr":
            return check_range(int(p_item[1]), 1920, 2002)
        case "iyr":
            return check_range(int(p_item[1]), 2010, 2020)
        case "eyr":
            return check_range(int(int(p_item[1])), 2020, 2030)
        case "hgt":
            if p_item[1].endswith("cm") and check_range(int(p_item[1][:-2]), 150, 193):
                return True
            elif p_item[1].endswith("in") and check_range(int(p_item[1][:-2]), 59, 76):
                return True
        case "hcl":
            if len(regex_hcl.findall(p_item[1])) > 0:
                return True
        case "ecl":
            if p_item[1] in eye_colors:
                return True
        case "pid":
            if len(regex_pid.findall(p_item[1])) > 0:
                return True

    return False


def check_range(value, low, high):
    if value >= low and value <= high:
        return True

    return False


    # INIT
    # Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "04test.txt"
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
    if len(i.strip()) == 0 and len(passport.strip()) > 0:  # blank line means process
        error = validate(passport)
        if error == "":
            printGood(passport)
            total_count += 1
        else:
            printBad(passport + ": " + str(error))
        passport = ""
    else:
        passport = passport + " " + i

printOK(f"Total: {total_count:d}")
printOK("Time: %.2f seconds" % (timer()-start_time))
