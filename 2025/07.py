import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/07.txt"


def part1():
    
    beams = set()
    splits_count = 0

    # Find where the beam start
    beams.add(data[0].index('S'))
    for i in range(1, len(data)):
        line = data[i]
        for b in beams.copy():
            if line[b] == '^':
                splits_count += 1
                beams.remove(b)
                beams.add(b-1)
                beams.add(b+1)

    return splits_count

def part2():
    beams = {}

    # Find where the beam start
    beams[data[0].index('S')] = 1
    for i in range(1, len(data)):
        line = data[i]
        for b in list(beams.copy().keys()):
            if line[b] == '^':
                beam_count = beams[b]
                beams[b] -= beam_count
                if beams[b] == 0:
                    del beams[b]
                # split beam
                if b-1 in beams:
                    beams[b-1] += beam_count
                else:
                    beams[b-1] = beam_count
                if b+1 in beams:
                    beams[b+1] += beam_count
                else:
                    beams[b+1] = beam_count

    # count the number of results
    count = 0
    for b in beams.keys():
        count += beams[b]
    return count


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