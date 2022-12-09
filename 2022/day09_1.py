import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "09.txt"
dir_lookup = {
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0)
}


def move_tail(head, tail) -> Tuple[int, int]:
    tail_distance = tuple(map(lambda i, j: i - j, head, tail))
    if abs(tail_distance[0]) <= 1 and abs(tail_distance[1]) <= 1:
        return tail

    new_tail_x = tail[0]
    if tail_distance[0] > 0:
        new_tail_x += 1
    elif tail_distance[0] < 0:
        new_tail_x -= 1

    new_tail_y = tail[1]
    if tail_distance[1] > 0:
        new_tail_y += 1
    elif tail_distance[1] < 0:
        new_tail_y -= 1

    return (new_tail_x, new_tail_y)


def print_grid(head, tail, visited):
    for y in range(15, -15, -1):
        line = ""
        for x in range(-11, 15):
            char = '.'
            if (x, y) == head:
                char = 'H'
            elif (x, y) == tail:
                char = "T"
            elif (x, y) == (0, 0):
                char = 's'
            elif (x, y) in visited:
                char = '#'
            line += char
        printDebug(line)


def main():
    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    visited = set()
    head = (0, 0)
    tail = (0, 0)

    # HERE WE GO

    for instruction in data:
        direction, number_of_spaces = instruction.split()
        for i in range(int(number_of_spaces)):
            head = tuple(map(lambda i, j: i + j, head, dir_lookup[direction]))
            # Evaluate tail distance
            tail = move_tail(head, tail)
            visited.add(tail)
            clear()
            print_grid(head, tail, visited)

    printGood(len(visited))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
