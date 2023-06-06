
def print_board(board):
    print("     1   2   3")
    print("   " + "┏━━━┳━━━┳━━━┓")
    print("1  ┃ " + " │ ".join(board[0]) + " ┃")
    print("   ┣━━━╋━━━╋━━━┫")
    print("2  ┃ " + " │ ".join(board[1]) + " ┃")
    print("   ┣━━━╋━━━╋━━━┫")
    print("3  ┃ " + " │ ".join(board[2]) + " ┃")
    print("   ┗━━━┻━━━┻━━━┛")
    print()


def check_winner(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print("Гравець", current_player, "на вибір!")

        while True:
            move = input("Введіть координати руху (рядок стовпець): ")

            if len(move) != 3 or move[1] != " ":
                print("Невірний формат вводу. Спробуйте ще раз.")
                continue

            row, col = move[0], move[2]

            if row not in ["1", "2", "3"] or col not in ["1", "2", "3"]:
                print("Невірні координати. Спробуйте ще раз.")
                continue

            row = int(row) - 1
            col = int(col) - 1

            if board[row][col] != " ":
                print("Ця клітинка вже зайнята. Спробуйте ще раз.")
                continue

            break

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print("Гравець", current_player, "переміг!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("Гра закінчилась внічию!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
