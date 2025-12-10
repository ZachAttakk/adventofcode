import sys, re
from itertools import product
from timeit import default_timer as timer
from zUtils.utils import *
from z3 import Int, Optimize, sat

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/10.txt"

def read_schematic(line):
    
    # Extract lights (content between [])
    lights_match = re.search(r'\[(.*?)\]', line)
    lights = lights_match.group(1) if lights_match else ""
    # Convert # to True and . to False
    lights = [c == '#' for c in lights]
    
    # Extract joltage (content between {})
    joltage_match = re.search(r'\{(.*?)\}', line)
    joltage = [int(x) for x in joltage_match.group(1).split(',')] if joltage_match else []
    
    # Extract all switches (all groups between ())
    switches = []
    for match in re.finditer(r'\((.*?)\)', line):
        content = match.group(1)
        if ',' in content:
            switches.append([int(x) for x in content.split(',')])
        else:
            switches.append([int(content)])
    
    return lights, switches, joltage

def iter_combinations(switches, count=1):
        for combination in product(switches, repeat=count):
            yield combination

def do_z3(switches, goal):
    opt = Optimize()
    
    # Create integer variables for how many times each switch is pressed
    switch_vars = [Int(f's{i}') for i in range(len(switches))]
    
    # Each switch must be pressed 0 or more times
    for var in switch_vars:
        opt.add(var >= 0)
    
    # For each position in the goal, sum up contributions from all switches
    for pos in range(len(goal)):
        # Count how many times this position appears across all switches
        contributions = []
        for i, switch in enumerate(switches):
            if pos in switch:
                contributions.append(switch_vars[i])
        
        # The sum of contributions must equal the goal value
        if contributions:
            opt.add(sum(contributions) == goal[pos])
        else:
            # If no switch affects this position, goal must be 0
            opt.add(goal[pos] == 0)
    
    # Minimize the total number of switch presses
    total_presses = sum(switch_vars)
    opt.minimize(total_presses)
    
    # Solve
    if opt.check() == sat:
        model = opt.model()
        return model.eval(total_presses).as_long() # type: ignore
    else:
        return sys.maxsize  # No solution found


def part1():

    total_presses = []

    lights_goal = []
    switches = []
    
    for i in range(len(data)):
        line = data[i]
        lights_goal, switches, _ = read_schematic(line)

        lights_state = [False] * len(lights_goal)

        # Try all combinations of switches, recording shortest that meets goal
        min_switch_count = sys.maxsize

        count = 0
        while lights_state != lights_goal:
            count += 1
            printDebug(f"Line {i}: Trying combinations of length {count}")
            for switch_combination in iter_combinations(switches, count=count):
                # Reset lights state
                lights_state = [False] * len(lights_goal)
                # Toggle lights based on switch combination
                for switch in switch_combination:
                    # Toggle lights for this switch
                    for light_index in switch:
                        if 0 <= light_index < len(lights_state):
                            lights_state[light_index] = not lights_state[light_index]

                # Check if lights state matches goal
                if lights_state == lights_goal:
                    switch_count = len(switch_combination)
                    if switch_count < min_switch_count:
                        min_switch_count = switch_count
                        printDebug(f"Line {i}: Found new min switch count: {min_switch_count}")
                        break

        # Save the result
        total_presses.append(min_switch_count)
    
    return sum(total_presses)


def part2():
    total_presses = []

    joltage_goal = []
    switches = []
    
    for i in range(len(data)):
        line = data[i]
        _, switches, joltage_goal = read_schematic(line)

        joltage_state = [0] * len(joltage_goal)

        # use z3 to find minimal switch presses to reach joltage goal
        min_switch_count = sys.maxsize
        printDebug(f"Line {i}: Using Z3 to find minimal switch presses")
        switch_count = do_z3(switches, joltage_goal)

        # Save the result
        total_presses.append(switch_count)
    
    return sum(total_presses)
    


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