from collections import Counter


# s = input('Введите строку>').lower()
s = 'Проверка работы программы. 123. Всё хорошо! Наверно...Ъь'.lower()
print(s)
cnt = Counter(s)
print(cnt)
print(f'Введённая строка: {s}')


total = [['гласных', 'аеёиоуыэюя', 0],
         ['согласных', 'бвгджзйклмнпрстфхцчшщ', 0],
         ['"ь" и "ъ"', "ьъ", 0],
         ['цифр', '0123456789', 0],
         ['других символов', None, 0]]

for key, value in cnt.items():
    for i in range(len(total)):
        try:
            if key in total[i][1]:
                total[i][2] += value
                break
        except TypeError:
            total[i][2] += value

for v in total:
    print(f'Количество {v[0]}: {v[2]}')
