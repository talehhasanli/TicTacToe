def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        
        valid_move = False
        while not valid_move:
            row_input = input("Enter the row (1-3): ")
            col_input = input("Enter the column (1-3): ")

            if row_input.isdigit() and col_input.isdigit():
                row = int(row_input) - 1
                col = int(col_input) - 1

                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":
                        valid_move = True
                    else:
                        print("That cell is already occupied. Try again.")
                else:
                    print("Invalid input. Row and column values must be between 0 and 2.")
            else:
                print("Invalid input. Row and column values must be digits.")

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            game_over = True
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

play_game()
