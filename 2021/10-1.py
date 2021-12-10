import sys
from timeit import default_timer as timer
from zUtils.utils import *
from queue import LifoQueue

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day10.txt"
BRACKET_MATCHES: dict[str, str] = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
ERROR_SCORES: dict[str, int] = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def validate(line: str, break_on_fail: bool = True) -> int:
    error_score: int = 0
    brackets: LifoQueue = LifoQueue()
    for i in line:
        if i in BRACKET_MATCHES:
            # new open bracket
            brackets.put(i)
        else:
            # close bracket
            last: str = brackets.get()
            if i != BRACKET_MATCHES[last]:
                error_score += ERROR_SCORES[i]
                if break_on_fail:
                    break

    return error_score


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

# HERE WE GO
errors: List[int] = []
for line in data:
    validation = validate(line)
    if validation > 0:
        errors.append(validation)

printGood(f"Part 1 answer: {sum(errors)}")

printOK("Time: %.5f seconds" % (timer()-start_time))
score: int = 0
