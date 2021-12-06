import sys
from timeit import default_timer as timer
from zUtils.utils import *

data: list[str] = []

# FILENAME FOR INPUT DATA
INPUT_FILENAME = "day04.txt"


class Board:
    width: int
    values: List[dict]
    last_mark: int = 0
    called_bingo = False

    def __init__(self, values: List[str], width: int = 5, ) -> None:
        self.width = width
        self.set_values(values)

    def set_values(self, _lines: List[str]):
        self.values = []

        # This is some really ugly nested loops, but it works...

        for _l in _lines:
            for _x in range(0, self.width*3, 3):  # per value, assuming double digit
                self.values.append({'val': int(_l[_x:_x+2]), 'marked': False})

    def mark(self, val: int):
        for _v in self.values:
            if _v['val'] == val:
                self.last_mark = val
                _v['marked'] = True

    @property
    def rows(self):
        for _i in range(0, len(self.values), self.width):
            yield self.values[_i:_i+self.width]

    @property
    def columns(self):
        for _i in range(self.width):
            yield self.values[_i::self.width]

    @property
    def bingo(self) -> bool:
        if self.called_bingo:  # Only call bingo once
            return False

        for _r in self.rows:  # check each row
            _row_bingo = True
            for _i in _r:  # if it has a false, it's false
                if _i['marked'] == False:
                    _row_bingo = False
                    break
            # if still looping, must be true
            if _row_bingo:
                self.called_bingo = True
                return True

        for _c in self.columns:  # check each row
            _col_bingo = True
            for _i in _c:  # if it has a false, it's false
                if _i['marked'] == False:
                    _col_bingo = False
                    break
            # if still looping, must be true
            if _col_bingo:
                self.called_bingo = True
                return True

        # Haven't found a bingo
        return False

    @property
    def score(self) -> int:
        _points: int = 0
        for _v in self.values:
            if not _v['marked']:
                _points += _v['val']

        return _points * self.last_mark


def make_boards(board_data: List[str], width=5) -> List[Board]:
    _boards: List[Board] = []

    # Are bingo boards always square?
    for _board_start in range(0, len(board_data), width+1):  # per board, blank lines between
        _new_board: Board = Board(board_data[_board_start:_board_start+5], width)
        _boards.append(_new_board)
    return _boards


# INIT
# Code for startup
start_time = timer()
data = advent_init(INPUT_FILENAME, sys.argv)

# HERE WE GO
# We know the first line is the list of moves:
moves: List[int] = list(map(int, data[0].split(',')))

boards = make_boards(data[2:])
# Now we should have an array of boards so we can start playing moves

for _num in moves:
    [b.mark(_num) for b in boards]

    [printGood(f"BINGO! {b.score}") for b in boards if b.bingo]


printOK("Time: %.2f seconds" % (timer()-start_time))
