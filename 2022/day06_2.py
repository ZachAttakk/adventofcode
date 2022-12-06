import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME: str = "06.txt"


def find_start(stream: str, length: int) -> int:
    """Checks for a continuous segment of [length] characters that are all different.

    Args:
        stream (str): Data stream to check
        length (int): Length of sequence to find

    Returns:
        int: index of last digit after [length] different characters
    """
    for i in range(length, len(stream)):
        # character exists in the last 4 digits
        check_range = set(stream[i-length:i])
        if len(check_range) == length:
            return i
    return -1


def main():

    # INIT
    # Code for startup
    start_time = timer()
    data = advent_init(INPUT_FILENAME, sys.argv, clear_screen=True)

    # HERE WE GO
    for entry in data:
        printGood(f"{find_start(entry, 14)}: {entry}")

    printOK("Time: %.5f seconds" % (timer()-start_time))


if __name__ == "__main__":
    main()
