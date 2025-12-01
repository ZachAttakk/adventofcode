import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/01.txt"


def part1():

    zero_count = 0
    pos = 50
    steps = [(i[0], int(i[1:])) for i in data]

    for step in steps:
        if step[0] == 'R':
            pos += step[1]
            pos = pos % 100
        elif step[0] == 'L':
            pos -= step[1]
            while pos < 0:
                pos += 100
        if pos == 0:
            zero_count += 1

    return zero_count

def part2():
    zero_count = 0
    pos = 50
    last_post = 50
    steps = [(i[0], int(i[1:])) for i in data]

    for step in steps:
        last_post = pos
        if step[0] == 'R':
            pos += step[1]
            while pos > 100:
                zero_count += 1
                pos -= 100
        elif step[0] == 'L':
            pos -= step[1]
            while pos < 0:
                if last_post == 0:
                    pos += 100
                    last_post = -1
                else:
                    zero_count += 1
                    pos += 100

        if pos == 100 or pos == 0:
            zero_count += 1
            pos = 0

    return zero_count
    


if __name__ == "__main__":
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    if len(data) == 0:
        printDisaster("No data found!")
        quit()

    part1_ans = part1()
    printGood(f"Part 1 Answer: {part1_ans}")
    part1_time = (timer()-start_time)
    printOK("Time: %.5f seconds" %part1_time)

    
    part2_ans = part2()
    printGood(f"Part 2 Answer: {part2_ans}")
    part2_time = (timer()-start_time) - part1_time
    printOK("Time: %.5f seconds" %part2_time)

    total_time = timer() - start_time
    printOK("Total Time: %.5f seconds" %total_time)