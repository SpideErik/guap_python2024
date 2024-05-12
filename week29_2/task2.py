import re


s = ' ' + input('Введите строку>')
print(re.findall(r'\W([A-ZА-ЯЁ]{2,})', s))
