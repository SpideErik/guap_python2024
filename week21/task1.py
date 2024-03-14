import time


def ask_time():
    while True:
        try:
            res = int(input('Время работы>'))
            if res > 0:
                return res
        except ValueError:
            pass
        print('Неверное значение')


t = ask_time()
print('Таймер запущен')

# for i in range(t, 0, -1):
#     print(f'Остановится через {i}')
#     time.sleep(1)

while t > 0:
    print(f'Остановится через {t}')
    time.sleep(1)
    t -= 1

print('Остановлен')
