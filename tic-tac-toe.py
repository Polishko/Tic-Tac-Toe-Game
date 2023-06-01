from math import ceil


def get_valid_player_sign():
    print("Player one, would you like to play with 'X' or 'O'?: ")
    while True:
        sign = input().capitalize()
        if sign != "X" and sign != "O":
            print("Enter 'X' or 'O':")
            continue
        else:
            break

    return sign


def get_player_choice(a):
    print(f"{a[0]} choose a free position [1-9]: ")
    while True:
        try:
            val = int(input())
        except ValueError:
            print("Enter a valid value:")
            continue
        if not 1 <= val <= 9:
            print("Value out of range/ Enter new value: ")
            continue
        if game_board[ceil(val / 3) - 1][(val % 3) - 1] != " ":
            print("Slot full/Choose another slot: ")
            continue
        else:
            return val


def setup():
    global player_one, player_two
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    player_one_sign = get_valid_player_sign()
    player_two_sign = "X" if player_one_sign == "O" else "O"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("This is the numeration of the board")
    [print(f"| {i} | {i + 1} | {i + 2} |") for i in range(1, 8, 3)]
    print(f"{player_one_name} starts first!")


def draw_board(board):
    for row in board:
        print("| ", end="")
        print(" | ".join([str(x) for x in row]), end="")
        print(" |")


def check_if_won(current, board):
    global loop
    first_row = all([x == current[1] for x in board[0]])
    second_row = all([x == current[1] for x in board[1]])
    third_row = all([x == current[1] for x in board[2]])
    first_column = all(x == current[1] for x in [board[0][0], board[1][0], board[2][0]])
    second_column = all(x == current[1] for x in [board[0][1], board[1][1], board[2][1]])
    third_column = all(x == current[1] for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == current[1] for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == current[1] for x in [board[0][2], board[1][1], board[2][0]])

    if any([first_row, second_row, third_row, first_column,
            second_column, third_column, first_diagonal, second_diagonal]):
        print(f"{current[0]} won!")
        loop = False


def check_if_draw(board):
    global loop
    if not any([item == " " for r in board for item in r]):
        print("It's a draw!")
        loop = False


def play(current, board):
    choice = get_player_choice(current)
    row = ceil(choice / 3) - 1
    col = (choice % 3) - 1
    board[row][col] = current[1]
    draw_board(board)
    check_if_won(current, board)
    check_if_draw(board)


player_one = None
player_two = None

game_board = [[" " for col in range(3)] for row in range(3)]
setup()
current_player = player_one
other = player_two
loop = True


while loop:
    play(current_player, game_board)
    current_player, other = other, current_player
