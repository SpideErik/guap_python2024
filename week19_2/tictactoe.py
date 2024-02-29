from random import randint


field = []
size = 0


def make_field():
    global field, size
    field = [[' ']*size for _ in range(size)]


def print_field():
    print('  '+' '.join(str(i) for i in range(1, size+1)))
    for y in range(size):
        print(f'{y+1} {" ".join(field[y])}')


def move(x, y, sym):
    global field, size
    x -= 1
    y -= 1
    if field[y][x] == ' ':
        field[y][x] = sym
        print('Ход сделан')
        return True
    print('Клетка занята')
    return False


def check_win():
    global field, size
    for y in range(size):
        for x in range(size):
            if y < size - 2:
                s = field[y][x] + field[y+1][x] + field[y+2][x]
                if s == 'XXX' or s == 'OOO':
                    return s
            if x < size - 2:
                s = field[y][x] + field[y][x+1] + field[y][x+2]
                if s == 'XXX' or s == 'OOO':
                    return s
            if y < size - 2 and x < size - 2:
                s = field[y][x] + field[y+1][x+1] + field[y+2][x+2]
                if s == 'XXX' or s == 'OOO':
                    return s
            if y < size - 2 and x > 1:
                s = field[y][x] + field[y+1][x-1] + field[y+2][x-2]
                if s == 'XXX' or s == 'OOO':
                    return s


def random_move(sym):
    while True:
        x = randint(1, size)
        y = randint(1, size)
        if move(x, y, sym):
            break


size = 5
make_field()
n = 0
print_field()
while n < size*size:
    random_move('X')
    print_field()
    win = check_win()
    if win:
        break
    n += 1
    if n >= size*size:
        break
    random_move('O')
    print_field()
    win = check_win()
    if win:
        break
    n += 1
print(win)
