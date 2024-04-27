a = int(input('Введите A>'))
b = int(input('Введите Б>'))

for b in range(a, b+1):
    print(f'Произведение: {a} * {b} = {a*b}')
    print(f'Степень: {a} в степени {b} = {a**b}')

