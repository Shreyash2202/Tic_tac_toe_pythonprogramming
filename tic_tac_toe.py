# Tic-Tac-Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")

    # Choose player symbols
    player1 = 'X'
    player2 = 'O'

    current_player = player1
    game_over = False

    while not game_over:
        print_board()

        # Get player's move
        if current_player == player1:
            move = int(input("Player 1 (X), choose your move (1-9): "))
        else:
            move = int(input("Player 2 (O), choose your move (1-9): "))

        # Validate the move
        if board[move-1] == ' ':
            board[move-1] = current_player
        else:
            print("Invalid move! Try again.")
            continue

        # Check if there is a winner
        if check_winner(board, current_player):
            print_board()
            print("Player", current_player, "wins!")
            game_over = True
        elif ' ' not in board:
            print_board()
            print("It's a tie!")
            game_over = True

        # Switch players
        current_player = player2 if current_player == player1 else player1

# Start the game
play_game()
