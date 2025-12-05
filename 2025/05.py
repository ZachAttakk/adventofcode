import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/05.txt"


def part1():

    # find break line
    id_start = 0
    for i, line in enumerate(data):
        if line.strip() == "":
            id_start = i
            break
    
    fresh_ranges: list[tuple[int, int]] = []
    # Procedd data into fresh ranges
    for line in data:
        if line.strip() == "":
            break
        start, end = line.split("-")
        fresh_ranges.append((int(start), int(end)))

    # check IDs for freshness
    fresh_ids: list[int] = []
    for line in data[id_start+1:]:
        id_to_check = int(line.strip())
        is_fresh = False
        for r in fresh_ranges:
            if r[0] <= id_to_check <= r[1]:
                is_fresh = True
                break

        if is_fresh:
            fresh_ids.append(id_to_check)

    return len(fresh_ids)


    


    
def part2():
    fresh_ranges: list[tuple[int, int]] = []
    # Procedd data into fresh ranges
    for line in data:
        if line.strip() == "":
            break
        start, end = line.split("-")
        fresh_ranges.append((int(start), int(end)))

    # remove overlap in ranges
    fresh_ranges.sort()
    merged_ranges: list[tuple[int, int]] = []
    for current in fresh_ranges:
        if not merged_ranges:
            merged_ranges.append(current)
        else:
            last_start, last_end = merged_ranges[-1]
            current_start, current_end = current
            if current_start <= last_end + 1:
                merged_ranges[-1] = (last_start, max(last_end, current_end))
            else:
                merged_ranges.append(current)

    # count total fresh IDs
    total_fresh = 0
    for r in merged_ranges:
        total_fresh += (r[1] - r[0] + 1)
    return total_fresh
    


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