import sys
from timeit import default_timer as timer
from zUtils.utils import *
from day14_1 import map_rock_line

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "14.txt"


def new_sand(rock, sand, sand_start, floor) -> tuple[int, int]:

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

        if sand_part[1] >= floor:  # tracked into the floor
            return last_pos

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
    # find out where the floor is
    floor = max([coord[1]+2 for coord in rock])

    # HERE WE GO
    sand_is_falling = True
    while sand_is_falling:
        new_sand_part = new_sand(rock, sand, sand_start, floor)
        if new_sand_part != sand_start:  # sand is covering the start
            sand.add(new_sand_part)
        else:
            sand_is_falling = False

    printGood(len(sand)+1)  # off by one because we didn't add the start

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
