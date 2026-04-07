from tic_tac_toe.board import Board

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.is_over = False
        self.winner = None

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def make_move(self, row, col):
        if self.is_over:
            return False
        if self.board.make_move(row, col, self.current_player.symbol):
            # проверяем победу
            if self.board.check_win(self.current_player.symbol):
                self.is_over = True
                self.winner = self.current_player
            # проверяем ничью
            elif self.board.is_draw():
                self.is_over = True
            else:
                self.switch_player()
            return True
        return False