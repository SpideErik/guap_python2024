from random import randint


n = int(input('n>'))
min_ = int(input('min>'))
max_ = int(input('max>'))

num = list(map(lambda x: randint(min_, max_), range(n)))
print(num)
print(list(filter(lambda x: x <= 0 and x % 2 == 0, num)))
print(list(filter(lambda x: x <= 0 and x % 2 != 0, num)))
print(list(filter(lambda x: x > 0 and x % 2 == 0, num)))
print(list(filter(lambda x: x > 0 and x % 2 != 0, num)))

double = []
for i in num:
    if num.count(i) > 1 and i not in double:
        double.append(i)
print(double)

abs_double = []
for i in num:
    if (num.count(i) > 1 or (i != 0 and num.count(-i)) > 0) and i not in abs_double:
        abs_double.append(i)
print(abs_double)
