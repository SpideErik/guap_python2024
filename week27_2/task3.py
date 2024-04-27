from random import randint


a = [randint(1, 20) for _ in range(10)]
b = [randint(1, 20) for _ in range(10)]

c = list(set(a) & set(b))

print(a)
print(b)
print(c)
