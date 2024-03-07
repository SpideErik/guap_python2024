from random import shuffle

lst1 = list(range(10))
lst2 = list(range(10))

while lst1.count('пусто') < 5 and lst2.count('пусто') < 5:
    shuffle(lst1)
    shuffle(lst2)
    print(f'Список 1: {lst1}\nСписок 2: {lst2}\n')
    for n, v in enumerate(zip(lst1, lst2)):
        if v[0] != v[1]:
            continue
        if n % 2 != 0:
            lst1[n] = 'пусто'
        else:
            lst2[n] = 'пусто'

if lst1.count('пусто') < lst2.count('пусто'):
    print('Победил список 1')
elif lst1.count('пусто') > lst2.count('пусто'):
    print('Победил список 2')
else:
    print('Ничья')

print(f'Список 1: {lst1}\nСписок 2: {lst2}')
