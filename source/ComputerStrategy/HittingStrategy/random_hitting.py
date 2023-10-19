import random

class RandomHitting:

    def __init__(self):
        self._cells = self._shuffle_cells()

    @staticmethod
    def _shuffle_cells():
        cells = list()
        for i in range(10):
            for j in range(10):
                cells.append((i, j))
        random.shuffle(cells)
        return cells

    def feedback(self, symbol):
        pass

    def hit(self):
        return self._cells.pop()
