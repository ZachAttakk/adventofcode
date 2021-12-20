import sys
from timeit import default_timer as timer
from typing import Set
from zUtils.utils import *
from copy import copy

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day17.txt"
CONST_GRAVITY: int = 1
CONST_DRAG: int = 1
CONST_VELOCITY_CUTOFF: int = 1000  # FIXME: Magic number
CONST_TRACE_DEPTH: int = 1000

# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)


def hit_trace_1D(velocity: int, resistance: int, target_min: int, target_max: int, cutoff: int = CONST_TRACE_DEPTH) -> bool:
    landing: int = 0
    for i in range(cutoff):
        landing += velocity
        velocity -= resistance
        if target_min <= landing <= target_max:
            return True
    else:  # if we reach this, then we didn't hit before we dropped below
        return False


def hit_trace_2D(velocity: List[int], resistance: List[int], target_min: List[int], target_max: List[int], cutoff: int = CONST_TRACE_DEPTH) -> bool:
    running_velocities: List[int] = copy(velocity)
    landing: List[int] = [0] * len(velocity)
    hits: List[bool] = [False] * len(velocity)
    for i in range(cutoff):
        for v in range(len(velocity)):
            landing[v] += running_velocities[v]
        # gravity is constant, water resistance approaches 0
        # TODO: If we can figure out how to apply gravity and drag differently,
        # this can be hit trace for n dimensions

        if running_velocities[0] != 0:
            running_velocities[0] = running_velocities[0] - resistance[0] \
                if velocity[0] > 0 else running_velocities[0] + resistance[0]
        running_velocities[1] -= resistance[1]

        for l in range(len(velocity)):
            hits[l] = target_min[l] <= landing[l] <= target_max[l]

        if all(hits):
            return True
    else:  # if we reach this, then we didn't hit before we dropped below
        return False


def max_height(velocity: int):
    height: int = 0
    last: int = height-1

    while height > last:
        last = height
        height += velocity
        velocity -= CONST_GRAVITY

    return last


def main():
    # HERE WE GO
    coords = data[0].split(',')
    x_min: int = int(coords[0][coords[0].find('x=')+2: coords[0].find('..')])
    x_max: int = int(coords[0][coords[0].find('..')+2:])
    y_min: int = int(coords[1][coords[1].find('y=')+2: coords[1].find('..')])
    y_max: int = int(coords[1][coords[1].find('..')+2:])

    # can launch hard enough to hit on first iteration
    init_y_velocity: int = min(y_min, 0)

    y_hitlist: List[int] = []
    for i in range(CONST_VELOCITY_CUTOFF):
        if hit_trace_1D(init_y_velocity, CONST_GRAVITY, y_min, y_max):
            y_hitlist.append(init_y_velocity)
        init_y_velocity += 1

    printOK(f"Potential Y coordinates: {len(y_hitlist)}")

    delta_x: int = 0
    if x_min > 0:
        delta_x = 1
    elif x_max < 0:
        delta_x = -1

    coordinate_hitlist: Set[Tuple[int, int]] = set()

    for n, y in enumerate(y_hitlist):
        init_x_velocity: int = 0
        printOK(f"{n} of {len(y_hitlist)}")

        for i in range(CONST_VELOCITY_CUTOFF):
            if hit_trace_2D([init_x_velocity, y],
                            [CONST_DRAG, CONST_GRAVITY], [x_min, y_min], [x_max, y_max]):
                coordinate_hitlist.add((init_x_velocity, y))
                printDebug(f"Found: {init_x_velocity, y}")

            init_x_velocity += delta_x

    printGood(f"Number of matches: {len(coordinate_hitlist)}")
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
