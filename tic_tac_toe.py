# Create the game board as a dictionary with keys as tuples of row and column indices
board = {(i, j): " " for i in range(3) for j in range(3)}

# Initialize the turn variable with "X"
turn = "X"

# Initialize the moves counter
moves = 0

# Continue the game loop until there is a winner or the board is full
while True:
    # Print the current state of the board
    for i in range(3):
        print(" | ".join(board[i, j] for j in range(3)))
        print("-" * 9)

    # Get the player's move
    row, col = map(int, input(f"Player {turn}'s turn. Enter row (0-2) and column (0-2) separated by space: ").split())

    # Check if the move is valid
    if board[row, col] == " ":
        # Update the board with the player's move
        board[row, col] = turn

        # Increment the moves counter
        moves += 1

        # Check if the player has won
        if any(all(board[i, j] == turn for j in range(3)) for i in range(3)) or \
           any(all(board[i, col] == turn for i in range(3)) for col in range(3)) or \
           all(board[i, i] == turn for i in range(3)) or \
           all(board[i, 2 - i] == turn for i in range(3)):
            print(f"Player {turn} wins!")
            break

        # Check if the board is full and it's a draw
        if moves == 9:
            print("It's a draw!")
            break

        # Switch the turn to the other player
        turn = "O" if turn == "X" else "X"
    else:
        print("Invalid move. Try again.")