import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []
connection_count = 1000

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "data/08.txt"

def get_distance(a,b):
    # calculate euclidean distance between two points in 3D space
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) ** 0.5


def part1():
    # Prep data

    nodes_list = []
    for line in data:
        nodes_list.append([int(x.strip()) for x in line.split(",")])

    # make a list of all nodes
    nodes = {}
    for i in range(len(nodes_list)):
        nodes[i] = nodes_list[i]

    # use that list to find the distances between each node
    distances = []
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            if i != j:
                dist = get_distance(nodes[i], nodes[j])
                distances.append((dist, i, j))

    # sort distances
    distances.sort(key=lambda x: x[0])


    # prepopulate circuits
    circuits = [[x] for x in range(len(nodes))]
    for con in range(connection_count):
        dist = distances[con]
        a = dist[1]
        b = dist[2]

        a_in_circuit = -1
        b_in_circuit = -1
        for c in range(len(circuits)):
            if a in circuits[c]:
                a_in_circuit = c
            if b in circuits[c]:
                b_in_circuit = c

        if a_in_circuit == -1 and b_in_circuit == -1:
            # neither in circuit, make new circuit
            circuits.append([a,b])
        elif a_in_circuit != -1 and b_in_circuit == -1:
            # a in circuit, add b
            circuits[a_in_circuit].append(b)
        elif a_in_circuit == -1 and b_in_circuit != -1:
            # b in circuit, add a
            circuits[b_in_circuit].append(a)
        elif a_in_circuit != b_in_circuit:
            # both in different circuits, merge
            circuits[a_in_circuit].extend(circuits[b_in_circuit])
            del circuits[b_in_circuit]

    # return length of 3 largest circuits
    circuits.sort(key=lambda x: len(x), reverse=True)
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

def part2():
    # Prep data

    nodes_list = []
    for line in data:
        nodes_list.append([int(x.strip()) for x in line.split(",")])

    # make a list of all nodes
    nodes = {}
    for i in range(len(nodes_list)):
        nodes[i] = nodes_list[i]

    # use that list to find the distances between each node
    distances = []
    for i in range(len(nodes)):
        for j in range(i, len(nodes)):
            if i != j:
                dist = get_distance(nodes[i], nodes[j])
                distances.append((dist, i, j))

    # sort distances
    distances.sort(key=lambda x: x[0])


    # prepopulate circuits
    circuits = [[x] for x in range(len(nodes))]
    for dist in distances:

        a = dist[1]
        b = dist[2]

        a_in_circuit = -1
        b_in_circuit = -1
        for c in range(len(circuits)):
            if a in circuits[c]:
                a_in_circuit = c
            if b in circuits[c]:
                b_in_circuit = c

        if a_in_circuit == -1 and b_in_circuit == -1:
            # neither in circuit, make new circuit
            circuits.append([a,b])
        elif a_in_circuit != -1 and b_in_circuit == -1:
            # a in circuit, add b
            circuits[a_in_circuit].append(b)
        elif a_in_circuit == -1 and b_in_circuit != -1:
            # b in circuit, add a
            circuits[b_in_circuit].append(a)
        elif a_in_circuit != b_in_circuit:
            # both in different circuits, merge
            circuits[a_in_circuit].extend(circuits[b_in_circuit])
            del circuits[b_in_circuit]

        # stop when they're all connected
        if len(circuits) <= 1:
            # return distance between X of last two nodes added
            return abs(nodes[a][0] * nodes[b][0])

    
    


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