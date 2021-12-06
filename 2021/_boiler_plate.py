import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "advent.txt"


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv)

# HERE WE GO


printOK("Time: %.2f seconds" % (timer()-start_time))
