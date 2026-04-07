import unittest
from tic_tac_toe.board import Board

class TestBoard(unittest.TestCase):
    def test_board_initialization(self):
        board = Board()
        self.assertEqual(len(board.cells), 3)
        for row in board.cells:
            self.assertEqual(len(row), 3)
            for cell in row:
                self.assertIsNone(cell)

    def test_make_move(self):
        board = Board()
        self.assertTrue(board.make_move(0, 0, 'X'))
        self.assertEqual(board.cells[0][0], 'X')
        self.assertFalse(board.make_move(0, 0, 'O'))

if __name__ == '__main__':
    unittest.main()