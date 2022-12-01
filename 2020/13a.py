import sys
from timeit import default_timer as timer
from os import path
from zUtils.utils import printOK, printDisaster, printGood, printBad


data: list[str] = []


def get_data(filename) -> list[str]:
    _data: list[str] = []
    if path.exists(filename):
        f = open(filename, "r", encoding='utf_8')
        if f.mode == 'r':
            _data: list[str] = f.read().splitlines()
            f.close()
    return _data


# INIT
# Code for startup
start_time = timer()
if len(sys.argv) < 2:
    FILENAME = "13.txt"
else:
    FILENAME = sys.argv[1]
data = get_data(FILENAME)
if not data:
    printDisaster("NO FILE")

# HERE WE GO
depart_time = int(data[0])
busses = data[1].split(',')
for i in range(len(busses)):
    if busses[i] == 'x':
        busses[i] = '0'
busses = list(map(int, busses))
schedule = [[]]*len(busses)

lowest_time = 10000
lowest_id = 0
for i in busses:
    if i != 0:
        cur_time = 0
        while cur_time < depart_time:
            cur_time += i
        if cur_time-depart_time < lowest_time:
            lowest_time = cur_time-depart_time
            lowest_id = i


printOK(lowest_time)
printGood(lowest_time * lowest_id)


printOK(f"Time: {(timer()-start_time):.4f} seconds")
