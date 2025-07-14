#!/usr/bin/python3


def print_board(board):
    """
    Prints the current tic-tac-toe board with clearer formatting.

    Parameters:
        board (list of list of str): 3x3 game board.
    """
    for i, row in enumerate(board):
        print(" " + " | ".join(row) + " ")
        if i < len(board) - 1:
            print("---+---+---")


def check_winner(board):
    """
    Checks if there is a winner on the board.

    Parameters:
        board (list of list of str): 3x3 game board.

    Returns:
        bool: True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def get_valid_int(prompt, valid_range):
    """
    Prompts the user for an integer input within a valid range.

    Parameters:
        prompt (str): The prompt message to display.
        valid_range (set or list): A collection of valid integer inputs.

    Returns:
        int: The validated integer input from the user.
    """
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if value not in valid_range:
                print(f"Please enter a valid number from {sorted(valid_range)}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def tic_tac_toe():
    """
    Runs the interactive Tic-Tac-Toe game between two players.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row = get_valid_int(f"Enter row (0, 1, or 2) for player {player}: ", {0, 1, 2})
        col = get_valid_int(
            f"Enter column (0, 1, or 2) for player {player}: ", {0, 1, 2}
        )

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That spot is already taken! Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
