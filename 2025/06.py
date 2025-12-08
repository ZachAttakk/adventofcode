import sys, re
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/06.txt"


def part1():
    # Rearrange values into arrays

    ops = {}
    for line in data:
        splitline = re.split(r"\s+", line.strip())

    # add each column to its own list
        for i in range(len(splitline)):
            if ops.get(i) is None:
                ops[i] = []

            ops[i].append(splitline[i])

    # do math on each column
    for key in ops.keys():
        col = ops[key]
        # do operation on col

        operation = col[-1]
        values = [int(x) for x in col[:-1]]
        if operation == "+":
            ops[key] = sum(values)
        elif operation == "*":
            result = 1
            for v in values:
                result *= v
            ops[key] = result
        else:
            printDisaster(f"Unknown operation: {operation}")
            return -1

    return sum(ops.values())

def part2():

    total = 0
    current_operation = []

    # start on the far right
    for i in range(len(data[0])-1, -1, -1):
        did_math = False
        # read down the lines
        number = ""
        for l in data:
            digit = l[i]
            match digit:
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    number += l[i]
                case "+" | "-" | "*" | "/":
                    # do the math
                    if digit == "+":
                        current_operation.append(int(number))
                        total += sum(current_operation)
                    elif digit == "*":
                        current_operation.append(int(number))
                        prod = 1
                        for n in current_operation:
                            prod *= n
                        total += prod

                    did_math = True

        if did_math:
            current_operation = []
        elif len(number) > 0:
            current_operation.append(int(number))
    
    return total
    


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