from math import ceil


def get_valid_player_sign():
    print("Oyuncu 1, 'X' veya 'O' ile mi oynamak istersin?: ")
    while True:
        sign = input().capitalize()
        if sign != "X" and sign != "O":
            print("Yanlis secim. 'X' veya 'O' gir:")
            continue
        else:
            break

    return sign


def get_player_choice(a):
    print(f"{a[0]}, bos bir kutu sec [1-9]: ")
    while True:
        try:
            val = int(input())
        except ValueError:
            print("Rakam girmelisin. Yeni deger gir:")
            continue
        if not 1 <= val <= 9:
            print("Boyle bir kutu yok/ Yeni kutu degeri gir: ")
            continue
        if game_board[ceil(val / 3) - 1][(val % 3) - 1] != " ":
            print("Kutu dolu/Yeni kutu sec: ")
            continue
        else:
            return val


def setup():
    global player_one, player_two
    player_one_name = input("Oyuncu 1 adi: ")
    player_two_name = input("Oyuncu 2 adi: ")
    player_one_sign = get_valid_player_sign()
    player_two_sign = "X" if player_one_sign == "O" else "O"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("Bunlar, oyun sirasinda kutu secmek icin kullanacagin numaralar.")
    [print(f"| {i} | {i + 1} | {i + 2} |") for i in range(1, 8, 3)]
    print(f"{player_one_name} basliyor!")


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
        print(f"{current[0]} kazandi!")
        loop = False


def check_if_draw(board):
    global loop
    if not any([item == " " for r in board for item in r]):
        print("Oyun berabere bitti")
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
