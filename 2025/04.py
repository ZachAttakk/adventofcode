import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

limit = 4

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/04.txt"

def is_reachable(x: int, y: int, grid: list[list[str]], limit: int) -> bool:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    steps = 0
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy


        if nx >= 0 and nx < len(grid[0]) and ny >= 0 and ny < len(grid):
            neighbor_value = grid[ny][nx]
            if neighbor_value == '@':
                steps += 1

            if steps >= limit:
                return False

    return True

def part1():
    grid = []
    for line in data:
        row = list(line)
        grid.append(row)

    total = 0

    output_grid = []
    
    for y in range(len(grid)):
        output_row = []
        for x in range(len(grid[y])):
            if grid[y][x] == '@' and is_reachable(x, y, grid, limit):
                total += 1
                output_row.append('x')
            else:
                output_row.append(grid[y][x])

        output_grid.append(output_row)

    return total
    

def part2():
    grid = []
    for line in data:
        row = list(line)
        grid.append(row)

    total = 0

    removable = sys.maxsize
    while removable > 0:
        output_grid = []
        
        # reset removable count
        removable = 0

        # go through grid and find reachable '@'
        for y in range(len(grid)):
            output_row = []
            for x in range(len(grid[y])):
                if grid[y][x] == '@' and is_reachable(x, y, grid, limit):
                    total += 1
                    removable += 1
                    output_row.append('x')
                else:
                    output_row.append(grid[y][x])

            output_grid.append(output_row)

        printDebug(f"Removable this iteration: {removable}")

        # remove marked 'x's from grid
        for y in range(len(output_grid)):
            for x in range(len(output_grid[y])):
                if output_grid[y][x] == 'x':
                    output_grid[y][x] = '.'

        # update grid for next iteration
        grid = output_grid
            
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