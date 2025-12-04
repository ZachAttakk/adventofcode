import sys
import operator

from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/03.txt"



def part1():

    total = 0
    for line in data:
        ints = [int(x) for x in line]
        digit_tens_index = -1
        digit_tens_value = -1
        digit_ones_value = -1
        for i in range(9,0,-1):
            if i in ints and ints.index(i) != len(ints)-1:
                digit_tens_index = ints.index(i)
                digit_tens_value = i
                break

        for i in range(digit_tens_index+1,len(ints)):
           if ints[i] > digit_ones_value:
               digit_ones_value = ints[i]
        
        highest_value = digit_tens_value * 10 + digit_ones_value
        total += highest_value

    return total


def part2():
    total = 0
    
    """ needed_total = 12
    needed_left = 12
    highest_index = -1

    indicies_used = []

    for line in data:
        values = [int(x) for x in line]
        for window in range(len(values)-needed_left+1):
            segment = values[window:window+needed_left]
            # find highest number in window
            highest_num = max(segment)
            indicies_used = segment.index(highest_num)
            
 """

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