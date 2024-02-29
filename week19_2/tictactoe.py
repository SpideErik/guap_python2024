from random import choice


field = [' ']*9
possible = list(range(9))  # возможные ходы для случайного выбора


def print_field():
    print('  123')
    for y in range(3):
        print(f'{y+1} {"".join(field[y*3:y*3+3])}')


def move(n, sym):
    global field
    if n not in possible:
        print('Клетка занята')
        return False
    possible.remove(n)
    field[n] = sym
    print(f'Ход сделан: {sym} -> {n % 3 + 1},{n // 3 + 1}')
    return True


# номера ячеек поля
# 012
# 345
# 678
win_row = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def check_win():
    for i in win_row:
        s = ''.join(field[j] for j in i)
        if s == 'XXX':
            return 'X'
        if s == 'OOO':
            return 'O'
    return None


def random_move(sym):
    move(choice(possible), sym)


def user_move(sym):
    while True:
        s = input('Ваш ход(yx)>')
        if len(s) == 2 and s.isnumeric() and 0 < int(s[0]) < 4 and 0 < int(s[0]) < 4:
            x = int(s[1])
            y = int(s[0])
            if move((y-1)*3 + (x-1), sym):
                return


names = {'1': ('случайный ход', random_move), '2': ('пользователь', user_move)}
players = [user_move, user_move]
symbols = ['X', 'O']


def ask_players():
    global players
    for i in names:
        print(f'{i}: {names[i][0]}')
    for i in range(2):
        s = input(f'Кто будет играть за {symbols[i]}>')
        players[i] = names[s][1]


ask_players()
n = 0
order = 0
print_field()
win = None
while n < 9:
    players[order](symbols[order])
    print_field()
    win = check_win()
    if win:
        break
    n += 1
    order ^= 1
if win:
    print('Выйграли', win)
else:
    print('Ничья')
