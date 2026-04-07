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