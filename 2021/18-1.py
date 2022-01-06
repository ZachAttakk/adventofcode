from functools import total_ordering
from sre_constants import RANGE
import sys
from timeit import default_timer as timer
import re
import math
from typing import Match
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day18.txt"
REGEX_PAIR: str = R"\[\d+,\s{0,1}\d+\]"
REGEX_OVER_TEN: str = R"(\d{2,})"
REGEX_LAST_NUMBER: str = R"(\d+)(?!.*\d)"
REGEX_STARTSWITH_NUMBER: str = R"^\d+"


def get_pair(number: str, index: int) -> List[int]:
    pairing_end: int = number.find(']', index)
    pairing_string: str = number[index:pairing_end]
    pairing_numbers: List[int] = eval(pairing_string)
    return pairing_numbers


def get_depth(number: str, index: int) -> int:
    return number[:index].count('[') - number[:index].count(']')


def check_explode(number: str) -> str:

    for match_position in re.finditer(REGEX_PAIR, number):
        if get_depth(number, match_position.start()) >= 4:
            #printDebug(f"Explode {match_position.group(0)}")
            pair: List[int] = eval(match_position.group(0))
            offset_left: int = 0

            # Add first number left
            last_number = re.search(REGEX_LAST_NUMBER, number[:match_position.start()])
            if last_number:
                number_to_replace: int = int(last_number.group(0))
                new_number_front: int = number_to_replace+pair[0]
                number = number[:last_number.start()] + str(new_number_front) + \
                    number[last_number.end():]
                offset_left = len(str(new_number_front))-len(str(number_to_replace))

            # Add first number right
            for i in range(match_position.end(), len(number)):
                next_number = re.match(REGEX_STARTSWITH_NUMBER, number[i:])
                if next_number:
                    new_number_back: int = pair[1] + int(next_number.group(0))
                    number = number[:i] + str(new_number_back) + number[next_number.end()+i:]
                    break

            # Replace with 0
            number = number[:match_position.start()+offset_left] + '0' + \
                number[match_position.end()+offset_left:]

            # Make sure we only check the first one
            break

    return number


def check_split(number: str) -> str:
    match_position: Match | None = re.search(REGEX_OVER_TEN, number)
    if match_position:
        #printDebug(f"Split {match_position.group(0)}")
        split_number = int(match_position.group(0))
        split_value: str = f"[{math.floor(split_number/2)}, {math.ceil(split_number/2)}]"
        number = number[:match_position.start()] + split_value + number[match_position.end():]

    return number


def calc_magnitude(number: str) -> str:

    current_number: str = number
    while True:
        match_position = re.search(REGEX_PAIR, current_number)
        if match_position == None:
            break
        else:
            # Resolve the pair
            pair: List[int] = eval(match_position.group(0))
            resolution: int = pair[0]*3 + pair[1]*2
            current_number = current_number.replace(match_position.group(0), str(resolution))

    return current_number


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

    # HERE WE GO
    current_number: str = data[0]

    for i in range(1, len(data)):
        current_number = f"[{current_number},{data[i]}]"
        still_reducing: bool = True

        while still_reducing:
            # printOK(current_number)
            last_number = current_number
            current_number = check_explode(current_number)
            if last_number == current_number:
                current_number = check_split(current_number)
                if last_number == current_number:
                    still_reducing = False

        printOK(current_number)

    # We've added up everything and reduced it all
    # Now calculate magnitude
    magnitude_result = calc_magnitude(current_number)
    printGood(magnitude_result)

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
