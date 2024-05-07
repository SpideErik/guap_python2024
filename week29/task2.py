import re


s = input('Введите строку с датой>')
dates = []
for i in re.findall(r'\d{2}\D\d{2}\D\d{4}|\d{2}\D\d{2}\D\d{2}', s):
    dates.append(re.sub(r'\D','.', i))
print(dates)
