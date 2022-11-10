import sys
from timeit import default_timer as timer
from os import path
from zUtils.utils import *

data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r")
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


def execute(code) -> tuple[int, int]:
    # code variables
    acc: int = 0
    index: int = 0

    running: bool = True
    runaway_stop = 0
    command_list = []
    # step through instructions one at a time
    while running:
        # prevent runaway loop
        runaway_stop += 1
        if runaway_stop > 10000:
            #printDisaster(f"Infinite loop!! Acc is {acc}")
            running = False
            return (2, acc)

        # have we been here?
        if index in command_list:
            #printBad(f"We've looped: {acc}")
            return (1, acc)
        # log which instruction was used
        command_list.append(index)

        # grab instructions
        # printOK(code[index])
        instruction: str = code[index][:3]
        amount: int = int(code[index][4:])

        # do a thing
        match instruction:
            case "acc":
                # change accumulator
                acc += amount
            case "jmp":
                # jump to line
                # remember to jump one less, so we can increase index at the end
                index += amount-1

        # increase index by one
        index += 1

        if index >= len(data):
            #printGood(f"Code Executed: {acc}")
            return (0, acc)

    # we should never get here
    return (3, acc)


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    filename = "day08.txt"
else:
    filename = sys.argv[1]
data = get_data(filename)
if (data == []):
    printDisaster("NO FILE")


# HERE WE GO

# error codes
# 0: All good
# 1: Loop detected
# 2: Runaway condition
# 3: Why did we not complete?

found = False
for i in range(len(data)):
    cur_code = data.copy()
    if cur_code[i].startswith("nop"):
        printOK(f"Changing nop to jmp {i}: {cur_code[i]}")
        cur_code[i] = cur_code[i].replace("nop", "jmp")
        result = execute(cur_code)
        if result[0] == 0:
            printGood(result)
            break
        else:
            printBad(result)


if not found:
    for i in range(len(data)):
        cur_code = data.copy()
        if cur_code[i].startswith("jmp"):
            printOK(f"Changing jmp to nop {i}: {cur_code[i]}")
            cur_code[i] = cur_code[i].replace("jmp", "nop")
            result = execute(cur_code)
            if result[0] == 0:
                found = True
                printGood(result)
                break
            else:
                printBad(result)

# AND WE'RE DONE
printOK("Time: %.2f seconds" % (timer()-start_time))
