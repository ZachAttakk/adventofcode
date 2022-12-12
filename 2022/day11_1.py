import math
import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "11.txt"


class Monkey:
    def __init__(self, monkey_text) -> None:
        self.items = list(map(int, monkey_text[1][monkey_text[1].index(':')+2:].split(', ')))
        self.operation = monkey_text[2][monkey_text[2].index('=')+2:]
        self.test = int(monkey_text[3][monkey_text[3].index('by')+3:])
        self.if_true = int(monkey_text[4][-1])
        self.if_false = int(monkey_text[5][-1])
        self.inspection_count = 0

    def __repr__(self) -> str:
        # return "Monkey "+str(self.items)
        return "Monkey "+str(self.inspection_count)

    def do(self, relief, mod_relief, monkeys):
        while len(self.items) > 0:

            self.inspection_count += 1

            i = self.items.pop(0)

            old = i
            i = eval(self.operation)
            if mod_relief:
                i = i % relief
            else:
                i = i // relief
            if i % self.test == 0:
                monkeys[self.if_true].catch(i)
            else:
                monkeys[self.if_false].catch(i)

    def catch(self, value):
        self.items.append(value)


def print_monkeys(monkeys):
    for m_i in range(len(monkeys)):
        printDebug(f"Monkey {m_i}: {monkeys[m_i]}")


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    monkeys = []
    for i in range(0, len(data), 7):
        monkeys.append(Monkey(data[i:i+6]))

    # HERE WE GO
    iterations = 20
    cut = 2
    relief = 3

    for iteration in range(iterations):
        for monkey in monkeys:
            monkey.do(relief, False, monkeys)
        clear()
        printDebug(f"Round {iteration+1}")
        print_monkeys(monkeys)

    monkeys_to_multiply = sorted(monkeys, key=lambda x: x.inspection_count)[-cut:]

    printGood(math.prod([i.inspection_count for i in monkeys_to_multiply]))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
