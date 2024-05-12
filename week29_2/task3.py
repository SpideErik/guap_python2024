import re


s = input('Введите строку>')
print(re.findall(r'\w+ма\w+|\w+ро\w+', s))
