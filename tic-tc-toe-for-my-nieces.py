from math import ceil
from pyfiglet import figlet_format
import fontstyle

title = {"3": "purple", "TAS": "yellow", "OYUNU": "green"}

for word, color in title.items():
    print(fontstyle.apply(figlet_format(word), color))


def start_game():
    global game_board
    game_board = [[" " for col in range(3)] for row in range(3)]
    setup()


def get_valid_player_sign():
    print(fontstyle.apply("Oyuncu 1, 'X' veya 'O' ile mi oynamak istersin?", "blue"))
  
    while True:
        sign = input().capitalize()
        if sign not in "X0O":
            print(fontstyle.apply("Yanlis secim. 'X' veya 'O' gir:", "red"))
            continue
        else:
            break

    return sign


def get_player_choice(a):
    print(f"{fontstyle.apply(a[0], 'blue')}, 1-9 arasinda bos bir kutu sec: ")
  
    while True:
        try:
            val = int(input())
        except ValueError:
            print(fontstyle.apply("Rakam girmelisin. Yeni deger gir:", "red"))
            continue
        if not 1 <= val <= 9:
            print(fontstyle.apply("Boyle bir kutu yok. Kutu icin yeni bir sayi gir:", "red"))
            continue
        if game_board[ceil(val / 3) - 1][(val % 3) - 1] != " ":
            print(fontstyle.apply("Bu kutu dolu. Yeni kutu sec:", "red"))
            continue
        else:
            return val


def setup():
    global player_one, player_two
  
    player_one_name = input("Oyuncu 1, adini yazar misin?: ")
    player_two_name = input("Oyuncu 2 adini yazar misin?: ")
    player_one_sign = get_valid_player_sign()
    player_two_sign = "X" if player_one_sign == "O" or player_one_sign == "0" else "O"
    player_one = [player_one_name, player_one_sign]
    player_two = [player_two_name, player_two_sign]
    print("Bunlar kutularin numaralari. Kutu secmek icin numarasini girmelisin.")
    [print(f"| {fontstyle.apply(i, 'blue')} | {fontstyle.apply(i + 1, 'blue')} | {fontstyle.apply(i + 2, 'blue')} |")\
     for i in range(1, 8, 3)]
    print(f"{fontstyle.apply(player_one_name, 'blue')} basliyor!")


def draw_board(board):
    for row in board:
        print("| ", end="")
        print(" | ".join([fontstyle.apply(str(x), "green") for x in row]), end="")
        print(" |")


def check_if_won(current, board):
    global loop
    global new_game
  
    rows = any([all(True if pos == current[1] else False for pos in r) for r in board])
    cols = any([all([board[r][c] == current[1] for r in range(3)]) for c in range(3)])
    first_diagonal = all([board[i][i] == current[1] for i in range(3)])
    second_diagonal = all([board[i][3 - i - 1] == current[1] for i in range(3)])

    if any([rows, cols, first_diagonal, second_diagonal]):
        print(fontstyle.apply(f"{current[0]} kazandi!", "cyan"))
        print("Tekrar oynamak icin 'E'ye bas;\ncikmak icin baska bir tusa bas")

        if input().capitalize() != "E":
            loop = False
        else:
            new_game = True

    else:
        check_if_draw(game_board)


def check_if_draw(board):
    global loop
    global new_game

    if not any([item == " " for r in board for item in r]):
        print(fontstyle.apply("Oyun berabere bitti", "purple"))
        print("Tekrar oynamak icin 'E'ye bas;\ncikmak icin baska bir tusa bas")

        if input().capitalize() != "E":
            loop = False
        else:
            new_game = True


def play(current, board):
    choice = get_player_choice(current)
    row = ceil(choice / 3) - 1
    col = (choice % 3) - 1
    board[row][col] = current[1]
    draw_board(board)
    check_if_won(current, board)


player_one, player_two = None, None
game_board = ""
start_game()
current_player = player_one
other = player_two

loop = True
new_game = False
while loop:
    play(current_player, game_board)
    current_player, other = other, current_player

    if new_game:
        start_game()
        current_player = player_one
        other = player_two
        new_game = False
