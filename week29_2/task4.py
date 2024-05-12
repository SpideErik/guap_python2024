import re


s = input('Введите строку>')
print(re.sub(r'<[^>]*>', '', s))
