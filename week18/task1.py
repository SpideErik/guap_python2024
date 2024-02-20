from random import randint


n = int(input('n>'))
num = list(map(lambda x: randint(1, 4), range(n)))

digits = []
for i in range(1, 5):
    digits.append([i]*num.count(i))

print(num)
print(digits)
