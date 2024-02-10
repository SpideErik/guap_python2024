import time
import os


arrow = '\\|/-\\|/-'
pos = [7, 8, 9, 15, 21, 20, 19, 13]
clock = ['8', ' ', '1', ' ', '2', '\n',
         ' ', ' ', ' ', ' ', ' ', '\n',
         '7', ' ', 'o', ' ', '3', '\n',
         ' ', ' ', ' ', ' ', ' ', '\n',
         '6', ' ', '5', ' ', '4',]


def print_clock(n):
    c = clock.copy()
    c[pos[n]] = arrow[n]
    print(''.join(c))


while True:
    for i in range(8):
        os.system('cls')
        print_clock(i)
        time.sleep(1)
