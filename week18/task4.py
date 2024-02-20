from random import randint


n = int(input('n>'))
min_ = int(input('min>'))
max_ = int(input('max>'))

giga_list = []
num = list(map(lambda x: randint(min_, max_), range(n)))
print(num)
giga_list.append(num)
giga_list.append(list(filter(lambda x: x < 0 and x % 2 == 0, num)))
print(giga_list[-1])
giga_list.append(list(filter(lambda x: x < 0 and x % 2 != 0, num)))
print(giga_list[-1])
giga_list.append(list(filter(lambda x: x >= 0 and x % 2 == 0, num)))
print(giga_list[-1])
giga_list.append(list(filter(lambda x: x >= 0 and x % 2 != 0, num)))
print(giga_list[-1])

double = []
for i in num:
    if num.count(i) > 1 and i not in double:
        double.append(i)
print(double)
giga_list.append(double)

abs_double = []
for i in num:
    if (num.count(i) > 1 or (i != 0 and num.count(-i)) > 0) and i not in abs_double:
        abs_double.append(i)
print(abs_double)
giga_list.append(abs_double)
