print("--------------------------")
print("Ultimate Python Tictactoe")
print("--------------------------")
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    print(f"\n   {board[0]}  |   {board[1]}   |  {board[2]}   ")
    print(" _____|_______|_____")
    print(f"   {board[3]}  |   {board[4]}   |  {board[5]}   ")
    print(" _____|_______|_____")
    print(f"   {board[6]}  |   {board[7]}   |  {board[8]}   ")
    print("      |       |      \n\n")

def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]            # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

current_player = "X"

while True:
    print_board()
    choose = input(f"Choose your position (Player {current_player})\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n-->")

    if choose in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = int(choose) - 1
        if board[position] == " ":
            board[position] = current_player
            if check_winner(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            if " " not in board:
                print_board()
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("\nThat position is already taken. Choose an empty position.")
    else:
        print("\nInvalid input. Please choose a position between 1 and 9.")

def clear_board():
    global board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

while True:
    print("--------------------------")
    print("Ultimate Python Tictactoe")
    print("--------------------------")
    clear_board()

    current_player = "X"

    while True:
        print_board()
        choose = input(f"Choose your position (Player {current_player})\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n-->")

        if choose in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = int(choose) - 1
            if board[position] == " ":
                board[position] = current_player
                if check_winner(current_player):
                    print_board()
                    print(f"Player {current_player} wins!")
                    break
                if " " not in board:
                    print_board()
                    print("It's a draw!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That position is already taken. Choose an empty position.")
        else:
            print("Invalid input. Please choose a position between 1 and 9.")

    if not play_again():
        print("Thank you for playing!")
        break
