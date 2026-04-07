import unittest
from tic_tac_toe.player import Player

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        p = Player('X')
        self.assertEqual(p.symbol, 'X')
        self.assertEqual(p.name, 'Player X')

if __name__ == '__main__':
    unittest.main()