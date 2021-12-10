import sys
from queue import LifoQueue
from statistics import median_low
from timeit import default_timer as timer

from zUtils.utils import *

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
COMPLETE_SCORES: dict[str, int] = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
SCORE_MULTIPLIER: int = 5


def validate(line: str, break_on_fail: bool = True) -> Tuple[bool, int]:
    score: int = 0
    validated = True

    brackets: LifoQueue = LifoQueue()
    for i in line:
        if i in BRACKET_MATCHES:
            # new open bracket
            brackets.put(i)
        else:
            # close bracket
            last: str = brackets.get()
            if i != BRACKET_MATCHES[last]:
                printDebug(f"Expected {BRACKET_MATCHES[last]}, found {i}")
                validated = False
                score += ERROR_SCORES[i]
                if break_on_fail:
                    break

    if validated:
        # positive score (probably)
        while brackets.qsize() > 0:
            last: str = brackets.get()
            printDebug(f"Closing {last} with {BRACKET_MATCHES[last]}")
            score = score*SCORE_MULTIPLIER+COMPLETE_SCORES[BRACKET_MATCHES[last]]

    return validated, score


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

# HERE WE GO
errors: List[int] = []
successes: List[int] = []
for line in data:
    success, score = validate(line)

    if success:
        printOK(f"Validation Success: {str(score)}")
        successes.append(score)
    else:
        printOK(f"Validation Failure: {str(score)}")
        errors.append(score)

printGood(f"Part 1 answer: {sum(errors)}")
printGood(f"Part 2 answer: {median_low(successes)}")

printOK("Time: %.5f seconds" % (timer()-start_time))
