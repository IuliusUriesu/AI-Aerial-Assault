from source.Board.board import Board
from source.ComputerStrategy.computer_strategy import ComputerStrategy
from source.Exceptions.exceptions import *
from source.Utilities.utilities import Utilities


class Game:

    def __init__(self, human: Board, computer: Board, strategy: ComputerStrategy):
        self._human = human
        self._computer = computer
        self._strategy = strategy
        self._offset = Utilities.init_offset()
        self._head = Utilities.plane_heads()
        self._make_human_board_visible()
        self._human_score = 0
        self._computer_score = 0

    def _make_human_board_visible(self):
        for i in range(10):
            for j in range(10):
                self._human.make_visible(i, j)

    def human_position_plane(self, row, column, orientation):
        if not self._human.on_board(row, column):
            raise OutsideBoardError('Plane outside board!')

        for off in self._offset[orientation]:
            i = row + off[0]
            j = column + off[1]
            if not self._human.on_board(i, j):
                raise OutsideBoardError('Plane outside board!')

        if self._human.get_symbol(row, column) != '.':
            raise PlaneOverlapError('Plane overlaps another plane!')

        for off in self._offset[orientation]:
            i = row + off[0]
            j = column + off[1]
            if self._human.get_symbol(i, j) != '.':
                raise PlaneOverlapError('Plane overlaps another plane!')

        self._human.set_symbol(row, column, self._head[orientation])
        for off in self._offset[orientation]:
            i = row + off[0]
            j = column + off[1]
            self._human.set_symbol(i, j, '*')

    def human_hit(self, row, column):
        if not self._computer.on_board(row, column):
            raise OutsideBoardError('Cell outside board!')

        symbol = self._computer.get_symbol(row, column)
        if symbol in [' ', '#', 'x']:
            raise AlreadyHitError('Cell already hit!')

        new_symbol = '?'
        if symbol == '.':
            new_symbol = ' '
        elif symbol == '*':
            new_symbol = '#'
        else:
            new_symbol = 'x'

        self._computer.set_symbol(row, column, new_symbol)
        self._computer.make_visible(row, column)
        if new_symbol == 'x':
            self._human_score += 1

    def computer_hit(self):
        row, column = self._strategy.hit()
        symbol = self._human.get_symbol(row, column)

        new_symbol = '?'
        if symbol == '.':
            new_symbol = ' '
        elif symbol == '*':
            new_symbol = '#'
        else:
            new_symbol = 'x'

        self._human.set_symbol(row, column, new_symbol)
        if new_symbol == 'x':
            self._computer_score += 1

        self._strategy.feedback(new_symbol)
        return row, column

    def winner(self):
        if self._human_score == 3:
            return 1
        elif self._computer_score == 3:
            return 2
        return 0

    def repr_human_board(self):
        board = '\n\tYour board:\n\n' + repr(self._human)
        return board

    def repr_both_boards(self):
        str1 = '\n\tYour board:\n\n' + repr(self._human)
        str2 = '\n\tEnemy board:\n\n' + repr(self._computer)

        split_lines1 = str1.split('\n')
        split_lines2 = str2.split('\n')

        str3 = ''
        for i in range(len(split_lines1)):
            line = split_lines1[i].center(30, ' ') + split_lines2[i].center(50, ' ')
            str3 += line + '\n'

        return str3
