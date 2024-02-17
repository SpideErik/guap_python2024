n = int(input('Введите кол-во покупок>'))
goods = []
for i in range(1, n+1):
    while True:
        words = input(f'Введите {i}-й товар и кол-во через пробел>').split()
        if len(words) == 2 and words[1].isdecimal():
            break
    goods.append([words[0], int(words[1])])
    print('Покупка добавлена в список')
    print(words)
print(goods)
