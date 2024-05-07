import re


s = input('Введите e-mail>')
r = re.fullmatch(r'\w{5,}@\w*mail\w*\.\w{2,3}', s)
print(r)
if r:
    print(f'Адрес {s} правильный')
else:
    print(f'Неверный адрес {s}')
