import sys
from timeit import default_timer as timer
from zUtils.utils import *
from dijkstar.algorithm import PathInfo
from dijkstar import Graph, find_path
from string import ascii_lowercase

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "12.txt"


def get_start_end(data):
    start = (0, 0)
    end = (0, 0)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 'S':
                start = (x, y)
            elif data[y][x] == 'E':
                end = (x, y)
    return {"start": start, "end": end}


def letters_to_numbers(letters):
    numbers = []
    for y in range(len(letters)):
        line = []
        for x in range(len(letters[0])):  # assuming square
            letter = letters[y][x]
            match letter:
                case 'S':
                    line.append(0)
                case 'E':
                    line.append(25)
                case _:
                    line.append(ascii_lowercase.find(letter))
        numbers.append(line)
    return numbers


def get_value(_grid: List[List[int]], coord: Tuple[int, int]) -> int:
    # sanity check
    if coord[0] < 0 or coord[0] >= len(_grid[0]) or coord[1] < 0 or coord[1] >= len(_grid):
        return -1

    # y on the outside
    return _grid[coord[1]][coord[0]]


def get_neighbours(_grid: List[List[int]], coord: Tuple[int, int]):

    neighbours: List[Tuple[int, int]] = []
    # because python doesn't include the last iteration in a loop
    for y in range(coord[1]-1, coord[1]+2):
        if y >= 0 and y < len(_grid):
            for x in range(coord[0]-1, coord[0]+2):
                if x >= 0 and x < len(_grid[0]) and coord != (x, y):
                    # exclude diagonals
                    if (x == coord[0] or y == coord[1]) and _grid[y][x] <= _grid[coord[1]][coord[0]]+1:
                        neighbours.append((x, y))
    return neighbours


def make_graph(matrix):
    graph = Graph()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            for n in get_neighbours(matrix, (x, y)):
                # not adding value because we're checking neighbours above
                #graph.add_edge((x, y), n, get_value(matrix, n))
                graph.add_edge((x, y), n, 1)

    return graph


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

    # map start to end
    pathinfo: PathInfo = find_path(graph, start_end["start"], start_end["end"])

    # first node is the starting node
    printGood(f"{len(pathinfo.nodes)-1}")

    # HERE WE GO
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
