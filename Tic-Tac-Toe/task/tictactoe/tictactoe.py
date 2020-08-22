temp = [" " for coord in range(9)]
x, y = None, None
turn = 1

board = [
    [temp[2], temp[5], temp[8]],
    [temp[1], temp[4], temp[7]],
    [temp[0], temp[3], temp[6]]
]


# print state of board
def print_board():
    print("---------")
    print("|", board[2][0], board[1][0], board[0][0], "|")
    print("|", board[2][1], board[1][1], board[0][1], "|")
    print("|", board[2][2], board[1][2], board[0][2], "|")
    print("---------")


# toggle player
def player_letter(turn):
    player = "O" if turn % 2 == 0 else "X"
    return player


# analyze user input
def valid_coord():
    global x, y
    global board
    global turn

    user_coord = input("Enter coordinates:")

    if len(user_coord.split()) != 2:
        print("You should enter numbers!")
        valid_coord()
    else:
        x, y = user_coord.split()
        if x.isdigit() and y.isdigit():
            if 1 <= int(x) <= 3 and 1 <= int(y) <= 3:
                coord_x = abs(int(x) - 3)
                coord_y = 3 - int(y)

                if board[coord_x][coord_y] != " ":
                    print("This cell is occupied! Choose another one!")
                    valid_coord()
                else:
                    board[coord_x][coord_y] = player_letter(turn)
                    turn += 1
                    print_board()
            else:
                print("Coordinates should be from 1 to 3!")
                valid_coord()
        else:
            print("You should enter numbers!")
            valid_coord()


def check_win():

    x_player = 0
    o_player = 0

    for row in board:
        for char in row:
            if char == 'X':
                x_player += 1
            elif char == 'O':
                o_player += 1


    x_wins = 0
    o_wins = 0
    draw = False
    #
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        x_wins += 1
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        o_wins += 1
    else:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == 'X' or board[0][i] == board[1][i] == board[2][i] == 'X':
                x_wins += 1
            elif board[i][0] == board[i][1] == board[i][2] == 'O' or board[0][i] == board[1][i] == board[2][i] == 'O':
                o_wins += 1

    if abs(x_player - o_player) >= 2:
        print('Impossible')
    elif x_wins and o_wins:
        print('Impossible')
    elif x_wins:
        print('X wins')
    elif o_wins:
        print('O wins')
    elif not x_wins and not o_wins and x_player + o_player == 9:
        draw = True
        print('Draw')
    elif not x_wins and not o_wins and x_player + o_player < 9:
        print('Game not finished')

    return x_wins, o_wins, draw


while True:
    print_board()
    valid_coord()
    x_wins, o_wins, draw = check_win()
    if x_wins > 0 or o_wins > 0 or draw:
        break
