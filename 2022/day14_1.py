import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "14.txt"


def map_rock_line(coordinates) -> set[tuple[int, int]]:

    new_coords = set()
    instructions = coordinates.split("->")
    nodes_for_rock = []
    for inst in instructions:
        nodes_for_rock.append(tuple(map(int, inst.strip().split(','))))

    for i in range(1, len(nodes_for_rock)):
        new_coords.update(map_single_line(nodes_for_rock[i-1], nodes_for_rock[i]))

    return new_coords


def map_single_line(start, end):
    nodes = []
    delta_x = 0
    if start[0] != end[0]:
        delta_x = 1 if end[0] > start[0] else -1

    delta_y = 0
    if start[1] != end[1]:
        delta_y = 1 if end[1] > start[1] else -1

    nodes.append(start)

    cur_x, cur_y = start
    while (cur_x, cur_y) != end:
        cur_x += delta_x
        cur_y += delta_y
        nodes.append((cur_x, cur_y))

    return nodes


def new_sand(rock, sand, sand_start) -> tuple[int, int]:
    sand_part = sand_start

    last_pos = (-1, -1)
    while sand_part != last_pos:
        last_pos = sand_part
        # check down one
        if (sand_part[0], sand_part[1]+1) not in rock and (sand_part[0], sand_part[1]+1) not in sand:
            sand_part = (sand_part[0], sand_part[1]+1)
        # check left and down
        elif (sand_part[0]-1, sand_part[1]+1) not in rock and (sand_part[0]-1, sand_part[1]+1) not in sand:
            sand_part = (sand_part[0]-1, sand_part[1]+1)
        # check right and down
        elif (sand_part[0]+1, sand_part[1]+1) not in rock and (sand_part[0]+1, sand_part[1]+1) not in sand:
            sand_part = (sand_part[0]+1, sand_part[1]+1)

        if sand_part[1] > 10000:  # probably assume it fell out the bottom
            return (-1, -1)

    return sand_part


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # map the rock face, entry by entry, getting all the coordinates in that series
    rock: set[tuple[int, int]] = set()
    for r in data:
        rock.update(map_rock_line(r))

    # set for where sand goes
    sand: set[tuple[int, int]] = set()

    sand_start = (500, 0)

    # HERE WE GO
    sand_is_falling = True
    while sand_is_falling:
        new_sand_part = new_sand(rock, sand, sand_start)
        if new_sand_part != (-1, -1):  # sand did settle
            sand.add(new_sand_part)
        else:
            sand_is_falling = False

    printGood(len(sand))

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
