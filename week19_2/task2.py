from random import sample, randint, choice

words = {3: ['мир', 'рай', 'лом', 'нос', 'лев'],
         4: ['хлеб', 'рука',  'часы', 'пила', 'ваза'],
         5: ['ложка', 'вилка', 'ручка', 'сушка', 'кисть']}


def make_field(size):
    field = []
    for y in range(size):
        field.append(['_']*size)
    return field


def print_field(field):
    for row in field:
        #print(row)
        print(''.join(row))


def put_h(word, field):
    """
    Размещаем слово по горизонтали
    :param word: Слово
    :return:
    """
    size = len(field)
    wl = len(word)
    while True:
        x = randint(0, size - wl)
        y = randint(0, size - 1)
        for n, i in enumerate(range(x, x + wl)):
            # либо пустая клетка, либо такая же как буква (пересечение слов)
            if field[y][i] != '_' and field[y][i] != word[n]:
                break
        else:
            field[y][x:x+wl] = word
            break


def put_v(word, field):
    """
    Размещаем слово по вертикали
    :param word: Слово
    :return:
    """
    size = len(field)
    wl = len(word)
    while True:
        y = randint(0, size - wl)
        x = randint(0, size - 1)
        for n, i in enumerate(range(y, y + wl)):
            # либо пустая клетка, либо такая же как буква (пересечение слов)
            if field[i][x] != '_' and field[i][x] != word[n]:
                break
        else:
            for n, i in enumerate(range(y, y + wl)):
                field[i][x] = word[n]
            return


letters = ''.join(chr(i) for i in range(ord('а'), ord('я')+1))


def fill_random(field):
    size = len(field)
    for y in range(size):
        for x in range(size):
            if field[y][x] == '_':
                field[y][x] = choice(letters)


f = make_field(10)
print_field(f)
print()

for i in range(3):
    put_v(choice(words[i+3]), f)
    put_h(choice(words[i+3]), f)

print_field(f)
print()

fill_random(f)

print_field(f)
