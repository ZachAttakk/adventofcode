#!/bin/python3.10
from dijkstar.algorithm import PathInfo
from zUtils.utils import *
import sys
from timeit import default_timer as timer
from dijkstar import Graph, find_path

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "day15.txt"
MAGNITUDE: int = 5


def get_value(_grid: List[List[int]], coord: Tuple[int, int]) -> int:
    # sanity check
    if coord[0] < 0 or coord[0] >= len(_grid[0]) or coord[1] < 0 or coord[1] >= len(_grid):
        return -1

    # y on the outside
    return _grid[coord[1]][coord[0]]


def get_neighbours(_grid: List[List[int]], coord: Tuple[int, int], include_diagonals=False):

    neighbours: List[Tuple[int, int]] = []
    # because python doesn't include the last iteration in a loop
    for y in range(coord[1]-1, coord[1]+2):
        if y >= 0 and y < len(_grid):
            for x in range(coord[0]-1, coord[0]+2):
                if x >= 0 and x < len(_grid[0]) and coord != (x, y):
                    # exclude diagonals
                    if (x == coord[0] or y == coord[1]) or include_diagonals:
                        neighbours.append((x, y))
    return neighbours


def make_graph(matrix):
    graph = Graph()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            for n in get_neighbours(matrix, (x, y)):
                graph.add_edge((x, y), n, get_value(matrix, n))

    return graph


def expand_matrix(matrix: List[List[int]], mag) -> List[List[int]]:
    size = len(matrix)
    output = [[0 for _x in range(size*mag)] for _y in range(size*mag)]

    # 5 by 5 tiles
    for y in range(mag):
        for x in range(mag):
            # repeat the actual grid, multiplying numbers by the outer iterations in 2 dimensions
            for b in range(size):
                for a in range(size):
                    # wrap 10s to 1, mod 10 gives a zero so need mod 9 +1
                    output[y*size + a][x*size + b] = (matrix[a][b] + y + x - 1) % 9 + 1

    return output


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=False)

# HERE WE GO
# Build a weightmap
matrix: List[List[int]] = [list(map(int, a)) for a in data]

matrix = expand_matrix(matrix, MAGNITUDE)

# prep the dijkstra graph
graph: Graph = make_graph(matrix)

# map top left (0,0) to bottom right (width, height)
pathinfo: PathInfo = find_path(graph, (0, 0), (len(matrix[0])-1, len(matrix)-1))

printGood(f"{pathinfo.total_cost}")

printOK("Time: %.5f seconds" % (timer()-start_time))
