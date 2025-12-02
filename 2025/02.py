import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/02.txt"


def part1():
    dupes_total = 0
    id_ranges = data[0].split(",")

    for id_range in id_ranges:
        start_id, end_id = map(int, id_range.split("-"))
        for item_id in range(start_id, end_id + 1):
            id_str = str(item_id)
            half_len = len(id_str) // 2

            # the first half matches the second half
            if len(id_str)%2 == 0 and id_str[0:half_len] == id_str[half_len:]:
                dupes_total += item_id

    return dupes_total

def part2():
    dupes_total = 0
    id_ranges = data[0].split(",")

    for id_range in id_ranges:
        start_id, end_id = map(int, id_range.split("-"))
        for item_id in range(start_id, end_id + 1):
            id_str = str(item_id)
            # range of subdivisions to check
            for split_size in range(1, len(id_str)//2 + 1):
                # split string into parts of split_size
                parts = [id_str[i:i+split_size] for i in range(0, len(id_str), split_size)]
                # check if all parts are the same
                if all(part == parts[0] for part in parts):
                    dupes_total += item_id
                    break
    return dupes_total
    


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