from random import sample, randint, choice

words = {3: ['мир', 'рай', 'лом', 'нос'], 4: ['хлеб', 'рука',  'часы', 'пила', 'ваза'], 5: ['ложка', 'вилка', 'ручка', 'сушка', 'кисть']}


def make_field():
    field = []
    for y in range(10):
        field.append(['_']*10)
        # field.append([])
        # for x in range(10):
        #     field[y].append('_')
    return field


def print_field(field):
    for row in field:
        print(row)


letters = ''.join(chr(i) for i in range(ord('а'), ord('я')+1))


def fill_random(field):
    for y in range(10):
        for x in range(10):
            if field[y][x] == '_':
                field[y][x] = choice(letters)


f = make_field()
print_field(f)

for i in range(3):
    while True:
        x = randint(0, 7-i)
        y = randint(0, 9)
        if f[y][x:x+3+i] == ['_']*(3+i):
            f[y][x:x+3+i] = choice(words[3+i])
            break

print_field(f)

fill_random(f)

print_field(f)
