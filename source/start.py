from source.Board.board import Board
from source.ComputerStrategy.HittingStrategy.probability_dfs_hitting import ProbabilityDFSHitting
from source.ComputerStrategy.PositioningStrategy.random_positioning import RandomPositioning
from source.ComputerStrategy.computer_strategy import ComputerStrategy
from source.Game.game import Game
from source.UI.ui import UI


if __name__ == '__main__':
    human = Board()
    computer = Board()

    positioning_strategy = RandomPositioning(computer)
    hitting_strategy = ProbabilityDFSHitting()
    strategy = ComputerStrategy(positioning_strategy, hitting_strategy)

    game = Game(human, computer, strategy)
    ui = UI(game)

    ui.start()
