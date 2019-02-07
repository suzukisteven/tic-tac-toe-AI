import random
player_1_wins = []
player_2_wins = []

def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    WIN_COMBINATIONS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    game_end = False
    current_player = ""

    def draw_board():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

    # def choose_player():
    #     current_player = input("Choose your player: ")

    # def turn_handler():
    #     if current_player == "X":
    #         move = choose_move()
    #         if board[move == "X" or board[move] == "O"]
    #             print("\nYou can't make that move. Try again.")
    #         else:
    #             board[move] = print(f"{current_player}")

    def player1():
        move = choose_move()
        if board[move] == "X" or board[move] == "O":
            print("\nYou can't make that move! Try again.")
            player1()
        else:
            board[move] = "X"

    def player2():
        move = ai_move()
        board[move] = "O"

    def ai_move():
        valid_move = False
        #
        while not valid_move:
            ai_move = random.randint(0,8)
            if board[ai_move] == "X" or board[ai_move] == "O":
                valid_move = False
            else:
                valid_move = True
        return ai_move


    def choose_move():
        while True:
            move = input()
            try:
                # Convert to int
                move = int(move)
                # Correct for array
                move -= 1
                # Return input for use in p1 p2
                if move in range(0, 9):
                    return move
                else:
                    print("\nHey, it's outta the board!")
                    continue
            except ValueError:
               print("\nIt asked for a number you fool.")
               continue

    def check_win():
        turn_number = 0
        for n in WIN_COMBINATIONS:
            if board[n[0]] == board[n[1]] == board[n[2]] == "X":
                player_1_wins.append(1)
                print("Player 1 (X) Wins!")
                print(f"Player 1 Wins: {len(player_1_wins)}\n")
                print(f"Player 2 Wins: {len(player_2_wins)}")
                return True

            if board[n[0]] == board[n[1]] == board[n[2]] == "O":
                player_2_wins.append(1)
                print("Player 2 (O) Wins!")
                print(f"Player 1 Wins: {len(player_1_wins)}\n")
                print(f"Player 2 Wins: {len(player_2_wins)}")
                return True

        for n in range(9):
            if board[n] == "X" or board[n] == "O":
                turn_number += 1
            if turn_number == 9:
                print("The game is a draw!\n")
                return True

    while not game_end:
        draw_board()
        game_end = check_win()
        if game_end == True:
            break
        print("It's Player 1's Turn (X)")
        player1()
        print()
        draw_board()
        game_end = check_win()
        if game_end == True:
            break
        print("AI Player's Turn (O)")
        player2()
        print()

    if input("Play again? (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()
