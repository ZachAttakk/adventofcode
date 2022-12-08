import sys
from timeit import default_timer as timer
from zUtils.utils import *
from day07_1 import Elf_dir_tree, Elf_dir, Elf_file, parse_structure

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "07.txt"


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # turn data into folder structure
    file_list = parse_structure(data)

    # HERE WE GO
    printGood(file_list.smallest_big_file(30000000))
    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
