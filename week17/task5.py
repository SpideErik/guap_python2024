available = {'бананы': 99, 'сосиски': 125, 'колбаса': 240, 'огурцы': 80, 'апельсины': 90,
             'гречка': 40, 'рис': 50, 'хлеб': 35, 'масло': 67}


def get_price(name: str):
    if name.lower() in available:
        return True, available[name.lower()]
    print(f'{name} не продается!')
    return False, 0


def print_purchase(goods):
    total = 0
    print('Товар           | Кол-во | Стоимость')
    for name, cnt, cost in goods:
        total += cost
        print(f'{name:16}| {cnt:6} | {cost:9}')
    print(f'Итого: {total}')


print('Доступные товары:')
print(available)

n = int(input('Введите кол-во покупок>'))
goods = []
for i in range(1, n+1):
    while True:
        words = input(f'Введите {i}-й товар и кол-во через пробел>').split()
        if len(words) == 2 and words[1].isdecimal():
            found, price = get_price(words[0])
            if found:
                cnt = int(words[1])
                item = [words[0], cnt, price*cnt]
                break
    goods.append(item)
    print('Покупка добавлена в список')
    print(item)

print_purchase(goods)
