import random

from source.Board.board import Board
from source.Utilities.utilities import Utilities


class ProbabilityDFSHitting:

    def __init__(self):
        self._offset = Utilities.init_offset()
        self._probability = self._init_probabilities()
        self._positions = self._init_positions()
        self._stack = list()
        self._last_hit = None
        self._tried = [[False for i in range(10)] for j in range(10)]

    def _init_probabilities(self):
        probability = [[0 for i in range(10)] for j in range(10)]

        for row in range(10):
            for column in range(10):
                for orientation in range(4):
                    valid_plane = True
                    for off in self._offset[orientation]:
                        i = row + off[0]
                        j = column + off[1]
                        if not Board.on_board(i, j):
                            valid_plane = False
                            break

                    if not valid_plane:
                        continue

                    probability[row][column] += 1
                    for off in self._offset[orientation]:
                        i = row + off[0]
                        j = column + off[1]
                        probability[i][j] += 1

        return probability

    def _init_positions(self):
        positions = list()

        for i in range(10):
            for j in range(10):
                positions.append((self._probability[i][j], i, j))

        positions.sort(reverse=True)
        return positions

    def feedback(self, symbol):
        row, column = self._last_hit

        if symbol == ' ':
            return
        elif symbol == '#':
            offset = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            random.shuffle(offset)

            for off in offset:
                i = row + off[0]
                j = column + off[1]
                if Board.on_board(i, j):
                    self._stack.append((i, j))
        else:   # symbol == 'x'
            self._stack.clear()

    def hit(self):
        while True:
            if len(self._stack) == 0:
                pos = len(self._positions) - 1
                for i in range(1, len(self._positions)):
                    if self._positions[i][0] != self._positions[0][0]:
                        pos = i - 1
                        break

                row, column = self._positions[random.randint(0, pos)][1:]
                break

            row, column = self._stack.pop()
            if not self._tried[row][column]:
                break

        self._last_hit = row, column
        self._tried[row][column] = True
        self._positions.remove((self._probability[row][column], row, column))
        return row, column
