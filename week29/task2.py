import re


s = input('Введите строку с датой>')
dates = []
for i in re.findall(r'\d{2}\D\d{2}\D\d{2,4}', s):
    dates.append(i[:2] + '.' + i[3:5] + '.' + i[6:])
print(dates)
