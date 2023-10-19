import time

from source.Game.game import Game
from source.Utilities.utilities import Utilities
from source.Exceptions.exceptions import *


class UI:

    def __init__(self, game: Game):
        self._game = game

    def start(self):
        self._welcome_message()
        self._human_position_planes()
        self._play_game()

    @staticmethod
    def _welcome_message():
        print('\nWelcome to Planes!')
        print('For drawing a plane, type the desired cell for its head. Example: C9')
        print('The orientation of a plane can be chosen by typing Up/Down/Left/Right. Example: Down')

    @staticmethod
    def _input_cell():
        print('Input a cell')
        cell = input('>>> ')
        cell = cell.strip().upper()
        return cell

    @staticmethod
    def _input_orientation():
        print('Input the orientation')
        orientation = input('>>> ')
        orientation = orientation.strip().lower()
        return orientation

    def _human_position_planes(self):
        dict_orientation = {'up': 0, 'down': 1, 'left': 2, 'right': 3}

        correct = 0
        while True:
            print(self._game.repr_human_board())

            if correct == 3:
                break

            cell = self._input_cell()

            try:
                Utilities.validate_cell(cell)
            except ValueError as ve:
                print(ve)
                continue

            row, column = Utilities.unpack_cell(cell)

            orientation = self._input_orientation()
            try:
                orientation = dict_orientation[orientation]
            except KeyError:
                print('Invalid orientation!')
                continue

            try:
                self._game.human_position_plane(row, column, orientation)
                correct += 1
            except OutsideBoardError as obe:
                print(obe)
            except PlaneOverlapError as poe:
                print(poe)

    def _play_game(self):
        turn = 0
        while True:
            print('\nWho starts the game?')
            print('\t1. You')
            print('\t2. Enemy')
            who = input('>>> ')
            who = who.strip()

            if who != '1' and who != '2':
                print('Invalid option!')
                continue

            turn = int(who)
            break

        while True:
            print(self._game.repr_both_boards())

            winner = self._game.winner()
            if winner == 1:
                print('CONGRATULATIONS! You WON the game.')
                break
            elif winner == 2:
                print('Game over! You lost...')
                break

            if turn == 1:
                while True:
                    cell = self._input_cell()
                    try:
                        Utilities.validate_cell(cell)
                    except ValueError as ve:
                        print(ve)
                        print()
                        continue

                    row, column = Utilities.unpack_cell(cell)
                    try:
                        self._game.human_hit(row, column)
                        break
                    except AlreadyHitError as ahe:
                        print(ahe)
                        print()

            else:
                print('Enemy thinks...')
                time.sleep(2.5)
                row, column = self._game.computer_hit()
                cell = Utilities.pack_cell(row, column)
                print('Enemy hit ' + cell + '!')

            turn = 3 - turn

