skills = {'Сила': 0, 'Интеллект': 0, 'Ловкость': 0, 'Хитрость': 0}
skill_names = ', '.join(skills)


def get_skill_name():
    while True:
        key = input(f'Выберите характеристику персонажа ({skill_names})>').title()
        if key in skills:
            return key
        print(f'{key} - такого нет!')


left = 10
while left > 0:
    print(f'Осталось {left} для распределения.')
    key = get_skill_name()
    n = int(input(f'На сколько увеличить характеристику {key}>'))
    if n < 1 or n > left:
        print('Неправильное значение')
        continue
    skills[key] += n
    print(f'{key} увеличена на {n}')
    left -= n


print('Создание персонажа завершено')
for key in skills:
    print(f'{key} = {skills[key]}')

