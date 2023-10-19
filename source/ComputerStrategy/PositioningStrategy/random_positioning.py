from source.Board.board import Board
import random
from source.Utilities.utilities import Utilities


class RandomPositioning:

    def __init__(self, board: Board):
        self._board = board
        self._offset = Utilities.init_offset()
        self._head = Utilities.plane_heads()

    def _position_plane(self):
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        orientation = random.randint(0, 3)

        if self._board.get_symbol(row, column) != '.':
            return False

        for off in self._offset[orientation]:
            i = row + off[0]
            j = column + off[1]

            if not self._board.on_board(i, j):
                return False

            if self._board.get_symbol(i, j) != '.':
                return False

        self._board.set_symbol(row, column, self._head[orientation])
        for off in self._offset[orientation]:
            i = row + off[0]
            j = column + off[1]
            self._board.set_symbol(i, j, '*')

        return True

    def position_planes(self):
        correct = 0
        while correct < 3:
            if self._position_plane() is True:
                correct += 1
