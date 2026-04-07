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

    def test_win_row(self):
        board = Board()
        # победа в ряду
        board.make_move(0, 0, 'X')
        board.make_move(0, 1, 'X')
        board.make_move(0, 2, 'X')
        self.assertTrue(board.check_win('X'))

    def test_win_col(self):
        # победа в столбце
        board = Board()
        board.make_move(0, 0, 'O')
        board.make_move(1, 0, 'O')
        board.make_move(2, 0, 'O')
        self.assertTrue(board.check_win('O'))

    def test_win_main_diagonal(self):
        board = Board()
        board.make_move(0, 0, 'X')
        board.make_move(1, 1, 'X')
        board.make_move(2, 2, 'X')
        self.assertTrue(board.check_win('X'))

    def test_win_sup_diagonal(self):
        # побочная диагональ
        board = Board()
        board.make_move(0, 2, 'O')
        board.make_move(1, 1, 'O')
        board.make_move(2, 0, 'O')
        self.assertTrue(board.check_win('O'))

    def test_not_win(self):
        # победы нет
        board = Board()
        board.make_move(0, 0, 'X')
        board.make_move(0, 1, 'O')
        board.make_move(0, 2, 'X')
        self.assertFalse(board.check_win('X'))

    def test_is_draw(self):
        board = Board()
        moves = [('O', 0, 0), ('X', 0, 1), ('O', 0, 2),
                 ('O', 1, 0), ('X', 1, 1), ('O', 1, 2),
                 ('X', 2, 0), ('O', 2, 1), ('X', 2, 2)]
        for p, r, c in moves:
            board.make_move(r, c, p)
        self.assertTrue(board.is_draw())

if __name__ == '__main__':
    unittest.main()