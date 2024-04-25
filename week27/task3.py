def ask_segment(name):
    x1 = int(input(f'Введите координату 1 отрезка {name}>'))
    x2 = int(input(f'Введите координату 2 отрезка {name}>'))
    return min(x1, x2), max(x1, x2)


a = ask_segment('A')
b = ask_segment('B')

if b[0] < a[0]:
    a, b = b, a

if a[1] < b[0]:
    print('Отрезки не пересекаются')
elif a[1] == b[0]:
    print(f'Отрезки имеют общую точку {b[0]}')
else:
    print(f'Отрезки имеют общую часть {b[0]} - {min(a[1], b[1])}')
