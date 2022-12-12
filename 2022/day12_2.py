import sys
from timeit import default_timer as timer
from zUtils.utils import *
from dijkstar.algorithm import PathInfo
from dijkstar import Graph, find_path
from string import ascii_lowercase
from day12_1 import get_start_end, letters_to_numbers, get_neighbours, get_value, make_graph

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "12.txt"


def get_start_candidates(grid):
    candidates = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                candidates.append((x, y))
    return candidates


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # first convert the data to numbers.
    data_grid = letters_to_numbers(data)

    # get start and end
    start_end = get_start_end(data)

    # prep the dijkstra graph
    graph: Graph = make_graph(data_grid)

    shortest_start = 10000
    for st in get_start_candidates(data_grid):
        try:
            pathinfo: PathInfo = find_path(graph, st, start_end["end"])

            if len(pathinfo.nodes)-1 < shortest_start:
                shortest_start = len(pathinfo.nodes)-1
        except:
            printDebug(f"No path from {st}")

    # first node is the starting node
    printGood(shortest_start)

    # HERE WE GO
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
