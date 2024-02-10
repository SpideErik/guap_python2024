import time
import os


arrow = '\\|/-\\|/-'
pos = [2, 3, 4, 10, 16, 15, 14, 8]
clock = ['8 1 2\n',
         ' ', ' ', ' ', ' ', ' ', '\n',
         '7', ' ', 'o', ' ', '3', '\n',
         ' ', ' ', ' ', ' ', ' ', '\n',
         '6 5 4']


def print_clock(n):
    c = clock.copy()
    c[pos[n]] = arrow[n]
    print(''.join(c))


while True:
    for i in range(8):
        os.system('cls')
        print_clock(i)
        time.sleep(1)
