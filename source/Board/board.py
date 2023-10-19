class Board:

    def __init__(self):
        self._data = [['.' for i in range(10)] for j in range(10)]
        self._visible = [[False for i in range(10)] for j in range(10)]
        # Cell symbols:
        # ' ' - air
        # '#' - hit
        # 'x' - dead
        # '*' - part of plane
        # '>', '<', '^', 'v' - head of plane
        # '.' - not visible yet

    def get_symbol(self, row: int, col: int):
        return self._data[row][col]

    def set_symbol(self, row: int, col: int, symbol: chr):
        self._data[row][col] = symbol

    def make_visible(self, row: int, col: int):
        self._visible[row][col] = True

    @staticmethod
    def on_board(row: int, col: int) -> bool:
        if 0 <= row < 10 and 0 <= col < 10:
            return True
        return False

    def __repr__(self):
        board  = '\t  1 2 3 4 5 6 7 8 9 10\n'

        for i in range(10):
            board += '\t' + chr(ord('A') + i) + ' '
            for j in range(10):
                if self._visible[i][j]:
                    board += self._data[i][j] + ' '
                else:
                    board += '. '
            board += '\n'

        return board
