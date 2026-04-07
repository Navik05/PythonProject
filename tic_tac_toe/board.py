class Board:
    def __init__(self):
        self.cells = [[None for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        if self.cells[row][col] is None:
            self.cells[row][col] = player
            return True
        return False

    def check_win(self, player):
        # строки
        for i in range(3):
            if all(self.cells[i][j] == player for j in range(3)):
                return True
        # столбцы
        for i in range(3):
            if all(self.cells[j][i] == player for j in range(3)):
                return True
        # главная диагональ
        if all(self.cells[i][i] == player for i in range(3)):
            return True
        # побочная диагональ
        if all(self.cells[i][2 - i] == player for i in range(3)):
            return True
        return False