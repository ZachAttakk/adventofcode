import sys
from timeit import default_timer as timer
from zUtils.utils import *
from day09_1 import move_tail, dir_lookup

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "09.txt"


def print_grid(snake, visited):
    for y in range(15, -15, -1):
        line = ""
        for x in range(-11, 15):
            char: str = '.'
            if (x, y) == (0, 0):
                char = 's'
            elif (x, y) in visited:
                char = '#'

            for i in range(len(snake), 0, -1):
                if (x, y) in snake:
                    char = str(snake.index((x, y)))

            if (x, y) == snake[0]:
                char = 'H'

            line += char
        printDebug(line)


def main():
    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    visited = set()
    snake: List[Tuple[int, int]] = [(0, 0) for i in range(10)]

    # HERE WE GO

    for instruction in data:
        direction, number_of_spaces = instruction.split()
        for i in range(int(number_of_spaces)):
            snake[0] = tuple(map(lambda i, j: i + j, snake[0], dir_lookup[direction]))
            # Evaluate tail distance
            for i in range(1, len(snake)):
                snake[i] = move_tail(tuple(snake[i-1]), snake[i])

            visited.add(snake[-1])
            clear()
            print_grid(snake, visited)

    printGood(len(visited))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
