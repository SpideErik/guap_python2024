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


def yx2i(y, x):
    return (y - 1) * 3 + (x - 1)


def check_win(field):
    for i in win_row:
        s = ''.join(field[j] for j in i)
        if s == 'XXX':
            return 'X'
        if s == 'OOO':
            return 'O'
    return None


def check_next_win(sym):
    for i in possible:
        tmp = field.copy()
        tmp[i] = sym
        if check_win(tmp):
            return i
    return None


def make_fork(sym):
    for i in possible:
        n = 0
        pos = possible.copy()
        pos.remove(i)
        tmp1 = field.copy()
        tmp1[i] = sym
        for j in pos:
            tmp = tmp1.copy()
            tmp[j] = sym
            if check_win(tmp):
                n += 1
        if n > 1:
            return i
    return i


def random_move(sym):
    move(choice(possible), sym)


def user_move(sym):
    while True:
        s = input('Ваш ход(yx)>')
        if len(s) == 2 and s.isnumeric() and 0 < int(s[0]) < 4 and 0 < int(s[0]) < 4:
            x = int(s[1])
            y = int(s[0])
            if move(yx2i(y, x), sym):
                return


def prof_move(sym):
    # если центр свободен идем туда
    if yx2i(2,2) in possible:
        return move(yx2i(2, 2), sym)
    n = field.count(' ')
    if n == 8:
        # первый ход О, центр уже заняли, пойдем в угол
        return move(choice((0, 2, 6, 8)), sym)
    if n == 7:
        # второй ход X, первый был в центр
        pos = possible.copy()
        # если О пошли в угол нельзя ставить рядом
        if field[0] == 'O':
            pos = (2, 5, 6, 7, 8)
        elif field[2] == 'O':
            pos = (0, 3, 6, 7, 8)
        elif field[6] == 'O':
            pos = (0, 1, 2, 5, 8)
        elif field[8] == 'O':
            pos = (0, 1, 2, 3, 6)
        return move(choice(pos), sym)
    if n == 6:
        # второй ход 0
        i = check_next_win('X')
        if i is not None:
            return move(i, sym)
        # пойдем в другой угол, так чтобы образовалась пара
        if field[0] == field[8] == ' ':
            return move(choice((0, 8)), sym)
        else:
            return move(choice((2, 6)), sym)
    if n == 5:
        # третий ход X
        i = check_next_win('X')
        if i is not None:
            return move(i, sym)
        i = check_next_win('O')
        if i is not None:
            return move(i, sym)
        # делаем вилку
        return move(make_fork(sym), sym)
    if n == 4:
        # третий ход O
        i = check_next_win('O')
        if i is not None:
            return move(i, sym)
        i = check_next_win('X')
        if i is not None:
            return move(i, sym)
        return random_move(sym)
    if n == 3:
        # четвертый ход X
        i = check_next_win('X')
        if i is not None:
            return move(i, sym)
        return random_move(sym)
    return random_move(sym)


names = {'1': ('случайный ход', random_move), '2': ('пользователь', user_move), '3': ('профи', prof_move)}
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
    win = check_win(field)
    if win:
        break
    n += 1
    order ^= 1
if win:
    print('Выйграли', win)
else:
    print('Ничья')
