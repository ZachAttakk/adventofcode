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
        _new_line = [["".join(sorted(_a)) for _a in _b] for _b in _new_line]
        _displays.append(_new_line)

    return _displays


def order_digits(_wires) -> List[str]:
    """Returns the sequence of letters but in order from 0 to 9
    """
    _ordered_wires: List[set] = [set()] * 10

    for _wire in _wires:
        match len(_wire):
            case 2:  # 1
                _ordered_wires[1] = set(_wire)
            case 3:  # 7
                _ordered_wires[7] = set(_wire)
            case 4:  # 4
                _ordered_wires[4] = set(_wire)
            case 7:  # 8
                _ordered_wires[8] = set(_wire)

    # we need those values to calculate the next part

    for _wire in _wires:
        match len(_wire):
            case 6:
                # 0,6,9
                # If there's only 1 piece in 4 that's not in 0, it's 0
                if len(list(set(_wire).difference(_ordered_wires[4]))) == 2:  # 9
                    _ordered_wires[9] = set(_wire)
                else:
                    # 0 or 6
                    if len(list(_ordered_wires[1].difference(_wire))) == 1:
                        # 1 overleps a 0 completely, but not a 6
                        _ordered_wires[6] = set(_wire)
                    else:
                        _ordered_wires[0] = set(_wire)
            case 5:
                if all(_char in _wire for _char in _ordered_wires[1]):
                    # Only 3 has both right segments, same as 1
                    _ordered_wires[3] = set(_wire)
                else:
                    # There's only 1 piece in a 4 that's not in a 5
                    if len(list(_ordered_wires[4].difference(_wire))) == 1:  # 5?
                        _ordered_wires[5] = set(_wire)
                    else:
                        _ordered_wires[2] = set(_wire)

    # sets are unordered
    _results = ["".join(_a) for _a in _ordered_wires]
    return ["".join(sorted(_a)) for _a in _results]


def calc_value(_digits: List[str], number_to_calc: List[str]):
    _answer_str: str = ""
    for _n in number_to_calc:
        _answer_str += str(_digits.index(_n))

    return int(_answer_str)


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv)

# HERE WE GO
displays = parse_displays(data)

_total = 0

for _d in displays:
    _ordered = order_digits(_d[0])
    _value = calc_value(_ordered, _d[1])
    _total += _value
    printDebug(_value)

printGood(_total)

printOK("Time: %.2f seconds" % (timer()-start_time))
