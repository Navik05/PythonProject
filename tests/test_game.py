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