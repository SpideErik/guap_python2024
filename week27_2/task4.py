import time
import sys
import os

if sys.platform == 'linux':
    def cls():
        os.system('clear')
else:
    def cls():
        os.system('cls')


def print_net(w, h, odd):
    cnt = (w+3)//4
    s1 = ('/ \_' * cnt)[:w]
    s2 = ('\_/_' * cnt)[:w]

    if odd:
        s1, s2 = s2, s1

    for i in range(h//2):
        print(s1)
        print(s2)
    if h & 1:
        print(s1)


odd = 0
while True:
    cls()
    print_net(80, 25, odd)
    odd = 1 - odd
    time.sleep(0.2)
