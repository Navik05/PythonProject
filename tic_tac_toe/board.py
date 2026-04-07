class Board:
    def __init__(self):
        self.cells = [[None for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        if self.cells[row][col] is None:
            self.cells[row][col] = player
            return True
        return False