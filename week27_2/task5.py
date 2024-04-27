import time
from random import randint


def print_rope(rl, x):
    if x < 0:
        x = 0
    elif x >= rl:
        x = rl - 1
    s = '-' * x + '0' + '-'*(rl - x - 1)
    print(s, end='\r', flush=True)


w = int(input('Длина веревки>'))
if w % 2 == 0:
    w += 1
x = w // 2
print_rope(w, x)

while 0 < x < w - 1:
    time.sleep(0.5)
    x += randint(-3, 3)
    print_rope(w, x)

print()
if x < 1:
    print('Выиграла левая сторона')
else:
    print('Выиграла правая сторона')
