def ask_fighter(name):
    m = int(input(f'Введите массу бойца {name}>'))
    if m <= 70:
        return 0, 'Легкий вес'
    if m <= 100:
        return 1, 'Средний вес'
    return 2, 'Тяжелый вес'


def check_fight(f1, f2):
    if f1[0] == f2[0]:
        print(f'Оба бойца в одной категории: {f1[1]}')
        return
    if abs(f1[0] - f2[0]) < 2:
        print(f'Разрешён нетитульный бой, разница в весе допустима. боец 1: {f1[1]}. боец 2: {f2[1]}')
        return
    print(f'Бой запрещен, большая разница в весе. боец 1: {f1[1]}. боец 2: {f2[1]}')


f1 = ask_fighter('N1')
f2 = ask_fighter('N2')
check_fight(f1, f2)
