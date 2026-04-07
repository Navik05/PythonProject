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