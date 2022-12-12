import math
import sys
from timeit import default_timer as timer
from zUtils.utils import *
from day11_1 import Monkey, print_monkeys

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "11.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    monkeys = []
    for i in range(0, len(data), 7):
        monkeys.append(Monkey(data[i:i+6]))

    # HERE WE GO
    iterations = 10000
    cut = 2
    relief = 1

    # Relief needs to be the lowest common multiple of all the monkeys
    # That way we can keep the numbers small but they still pass all the tests
    relief = math.prod(list([m.test for m in monkeys]))

    for iteration in range(iterations):
        for monkey in monkeys:
            monkey.do(relief, True, monkeys)
            if (iteration+1) % 1000 == 0:
                clear()
                printDebug(f"Round {iteration+1}")
                print_monkeys(monkeys)

    monkeys_to_multiply = sorted(monkeys, key=lambda x: x.inspection_count)[-cut:]

    printGood(math.prod([i.inspection_count for i in monkeys_to_multiply]))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
