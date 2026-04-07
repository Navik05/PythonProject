import unittest
from tic_tac_toe.game import Game
from tic_tac_toe.player import Player

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        p1 = Player('X')
        p2 = Player('O')
        game = Game(p1, p2)
        self.assertEqual(game.current_player, p1)
        self.assertFalse(game.is_over)

    def test_switch_player(self):
        p1 = Player('X')
        p2 = Player('O')
        game = Game(p1, p2)
        game.switch_player()
        self.assertEqual(game.current_player, p2)

    def test_make_move(self):
        p1 = Player('X')
        p2 = Player('O')
        game = Game(p1, p2)
        game.make_move(0, 0)
        self.assertEqual(game.board.cells[0][0], 'X')
        self.assertEqual(game.current_player, p2)

    def test_game_over_win(self):
        p1 = Player('X')
        p2 = Player('O')
        game = Game(p1, p2)
        game.make_move(0, 0)  # X
        game.make_move(0, 1)  # O
        game.make_move(1, 0)  # X
        game.make_move(0, 2)  # O
        game.make_move(2, 0)  # X победили
        self.assertTrue(game.is_over)
        self.assertEqual(game.winner, p1)

    def test_game_over_draw(self):
        p1 = Player('X')
        p2 = Player('O')
        game = Game(p1, p2)
        moves = [(0, 0), (0, 1), (0, 2),
                 (1, 1), (1, 0), (1, 2),
                 (2, 1), (2, 0), (2, 2)]
        for r, c in moves:
            game.make_move(r, c)
        self.assertTrue(game.is_over)
        self.assertIsNone(game.winner)