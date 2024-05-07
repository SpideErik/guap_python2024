import re


s = input('Введите строку с телефонами>')
phones = []
for i in re.findall(r'\d\D?\d{2,3}\D?\d{3}\D?\d{2}\D?\d{2}', s):
    phones.append(re.sub(r'\D', '', i))
print(phones)
