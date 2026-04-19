# Initialize empty board
board = [" "] * 9


def show_positions():
    print("\nBoard Positions:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8")
    print()


def print_board():
    print("\nCurrent Board:")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("Player 1 uses X")
    print("Player 2 uses O")
    show_positions()

    player = "X"
    moves_made = 0  # count only valid moves

    while moves_made < 9:  # only valid moves count toward max 9
        print_board()
        print("Player", player, "turn")
        move = input("Choose a position (0-8): ")

        # validate input
        if not move.isdigit():
            print("Please enter a number between 0 and 8.")
            continue

        move = int(move)

        if move < 0 or move > 8:
            print("Invalid position. Choose a number from 0 to 8.")
            continue

        if board[move] != " ":
            print("That position is already taken.")
            continue

        # place player symbol
        board[move] = player
        moves_made += 1  # only increment after a valid move

        # check if player won
        if check_winner(player):
            print_board()
            print("Player", player, "wins!")
            return

        # switch player
        player = "O" if player == "X" else "X"

    # if loop finishes, all 9 moves done → draw
    print_board()
    print("The game is a draw!")



tic_tac_toe()