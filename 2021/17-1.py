import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day17.txt"
CONST_GRAVITY: int = 1
CONST_DRAG: int = 1
CONST_Y_VELOCITY_CUTOFF: int = 100  # FIXME: Magic number

# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)


def hit_trace(velocity: int, target_min: int, target_max: int, cutoff: int = 10000) -> bool:
    landing: int = 0
    for i in range(cutoff):
        landing += velocity
        velocity -= CONST_GRAVITY
        if target_min <= landing <= target_max:
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

    init_y_velocity: int = 0  # so our first loop checks 0. Will it always be below us?
    highest_hit: int = 0
    for i in range(CONST_Y_VELOCITY_CUTOFF):
        init_y_velocity += 1
        if hit_trace(init_y_velocity, y_min, y_max):
            highest_hit = init_y_velocity

    init_y_velocity = highest_hit

    delta_x: int = 0
    if x_min > 0:
        delta_x = 1
    elif x_max < 0:
        delta_x = -1

    init_x_velocity: int = 0

    has_hit = hit_trace(init_x_velocity, x_min, x_max)
    while not has_hit:
        init_x_velocity += delta_x
        if hit_trace(init_x_velocity, x_min, x_max):
            has_hit = True

    printGood(f"Velocity: {init_x_velocity}, {init_y_velocity}: {max_height(init_y_velocity)}")

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
