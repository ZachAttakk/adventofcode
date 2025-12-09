import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/09.txt"


def part1():
    nodes = []
    for line in data:
        nodes.append([int(x.strip()) for x in line.split(",")])

    # find largest 2D area between two nodes
    max_area = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            a = nodes[i]
            b = nodes[j]
            # calculate area inclusive of the nodes themselves
            area = (abs(a[0]-b[0]) + 1) * (abs(a[1]-b[1]) + 1)
            if area > max_area:
                max_area = area
    return max_area

def part2():
    nodes = []
    for line in data:
        nodes.append([int(x.strip()) for x in line.split(",")])

    # find largest 2D area between two nodes
    max_area = 0
    
    # find min and max for each axis
    min_x = min([n[0] for n in nodes])
    max_x = max([n[0] for n in nodes])
    min_y = min([n[1] for n in nodes])
    max_y = max([n[1] for n in nodes])

    # build acceptable X ranges on each Y level
    for y in range(min_y, max_y+1):
        x_positions = []
        for n in nodes:
            if n[1] == y:
                # find min and max X for this Y
                x_positions.append(n[0])
        if len(x_positions) >= 2:
            x_positions.sort()
            area = (x_positions[-1] - x_positions[0] + 1)
            if area > max_area:
                max_area = area

    return max_area
    


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