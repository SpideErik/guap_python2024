import re


s = input('Введите строку>')
print(re.findall(r'\w+-\w+', s))
