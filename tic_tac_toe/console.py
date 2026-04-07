from tic_tac_toe.game import Game
from tic_tac_toe.player import Player

def display_board(board):
    print("\n  0 1 2")
    for i, row in enumerate(board.cells):
        print(f"{i} " + " ".join(cell if cell else '.' for cell in row))
    print()

def get_move(player):
    while True:
        try:
            move = input(f"{player.name} ({player.symbol}), введите строку и столбец: ")
            row, col = map(int, move.split(','))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Ошибка! Координаты могут быть от 0 до 2")
        except ValueError:
            print("Неверный ввод. Используйте формат ввода: строка, столбец")

def main():
    p1 = Player('X', "Игрок 1")
    p2 = Player('O', "Игрок 2")
    game = Game(p1, p2)

    while not game.is_over:
        display_board(game.board)
        row, col = get_move(game.current_player)
        if not game.make_move(row, col):
            print("Ячейка занята, попробуйте ещё раз")
    display_board(game.board)
    if game.winner:
        print(f"{game.winner.name} выиграл!")
    else:
        print("Ничья :)")

if __name__ == '__main__':
    main()