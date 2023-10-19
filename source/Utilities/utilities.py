class Utilities:

    def __init__(self):
        pass

    @staticmethod
    def init_offset():
        offset = list()
        offset.append([(1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, 0), (3, -1), (3, 0), (3, 1)])  # Up ^
        offset.append([(-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (-2, 0), (-3, -1), (-3, 0), (-3, 1)])  # Down v
        offset.append([(-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (0, 2), (-1, 3), (0, 3), (1, 3)])  # Left <
        offset.append([(-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1), (0, -2), (-1, -3), (0, -3), (1, -3)])  # Right >
        return offset

    @staticmethod
    def plane_heads():
        heads = ['^', 'v', '<', '>']
        return heads

    @staticmethod
    def validate_cell(cell: str):
        if len(cell) != 2 and len(cell) != 3:
            raise ValueError('Invalid cell!')

        if ord(cell[0]) < ord('A') or ord(cell[0]) > ord('J'):
            raise ValueError('Invalid cell!')

        if len(cell) == 2:
            if not cell[1].isdigit():
                raise ValueError('Invalid cell!')
            if cell[1] == '0':
                raise ValueError('Invalid cell!')
            return

        if cell[1] != '1' or cell[2] != '0':
            raise ValueError('Invalid cell!')

    @staticmethod
    def unpack_cell(cell: str):
        row = ord(cell[0]) - ord('A')
        column = int(cell[1:]) - 1
        return row, column

    @staticmethod
    def pack_cell(row: int, column: int):
        column += 1
        cell = chr(ord('A') + row) + str(column)
        return cell
