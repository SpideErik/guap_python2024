s1 = input('Введите строку>')
s2 = ''

if not s1.isalpha():
    print('Строка не соответствует условию')
    exit()

for n, sym in enumerate(s1):
    if n % 2 == 0:
        s2 += sym.upper()
    else:
        s2 += sym.lower()

print(s2)
