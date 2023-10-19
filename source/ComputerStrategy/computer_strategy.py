class ComputerStrategy:

    def __init__(self, positioning_strategy, hitting_strategy):
        self._positioning_strategy = positioning_strategy
        self._hitting_strategy = hitting_strategy
        self._positioning_strategy.position_planes()

    def hit(self):
        return self._hitting_strategy.hit()

    def feedback(self, symbol):
        self._hitting_strategy.feedback(symbol)
