import re


# words = input('Введите строку>').split()
s = input('Введите строку>')
words = re.split(r'\W+', s)
if words[-1] == '':
    words.pop()
print(words[0], words[-1])
