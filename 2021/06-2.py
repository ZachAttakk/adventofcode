import sys
from timeit import default_timer as timer
from collections import Counter
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "day06.txt"


def make_fish_list(_data_line: str, max_age: int):

    _fish_list: List[int] = []
    fishcounts = Counter(list(map(int, _data_line.split(','))))
    for _i in range(max_age+1):
        if _i in fishcounts:  # there's fish of this age
            _fish_list.append(fishcounts[_i])
        else:
            _fish_list.append(0)
    return _fish_list


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv)


# HERE WE GO
# Let's start with some constants
FISH_BORN_AGE: int = 8  # At what age to add new fish (max)
FISH_RESPAWN_AGE: int = 6  # At what age to put fish after giving birth
FISH_SPAWN_RATE: int = 1  # How many offsprint to birth from each fish
SIM_DAYS: int = 256  # how many day to simulate

fish_list: List[int] = make_fish_list(data[0], FISH_BORN_AGE)

# Here we actually run the simulation.
for _day in range(SIM_DAYS):
    # move everything down
    _births = fish_list.pop(0)
    # maintain list length
    fish_list.append(0)
    # add respawn fish back in
    fish_list[FISH_RESPAWN_AGE] += _births
    # add births according to birth rate
    fish_list[FISH_BORN_AGE] += _births * FISH_SPAWN_RATE
    # make it look cool
    printDebug(f"Day {_day+1}: {sum(fish_list)}")

printGood(f"End of Day {SIM_DAYS}: {sum(fish_list)}")

printOK("Time: %.5f seconds" % (timer()-start_time))
