class Player:
    def __init__(self, symbol, name=None):
        self.symbol = symbol
        self.name = name or f'Player {symbol}'