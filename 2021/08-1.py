import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "day08.txt"


def parse_displays(_data):
    _displays = []
    for _line in _data:
        _new_line = _line.split(' | ')
        _new_line = [_a.split(' ') for _a in _new_line]
        _displays.append(_new_line)

    return _displays


                # INIT
                # Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv)

# HERE WE GO
displays = parse_displays(data)

# For part 1 we only need to know which values are 1, 4, 7 and 8
# So we only care whether the length is 2, 3, 4 or 7
# There's probably a one-liner for this but I can't work it out
_digit_count: int = 0
for _line in displays:
    for _digit in _line[1]:
        if len(_digit) in (2, 3, 4, 7):
            _digit_count += 1

printGood(_digit_count)

printOK("Time: %.2f seconds" % (timer()-start_time))
