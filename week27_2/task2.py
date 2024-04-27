from math import modf

a = float(input('Введите A>'))
b = float(input('Введите Б>'))

r = a / b
f, i = modf(r)

print(f'Деление: {a} / {b} = {r}')
print(f'Целая часть: {i}, Дробная: {f}')
