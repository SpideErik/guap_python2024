import time


i = 0
while True:
    time.sleep(1)
    i += 1
    print(f'Время работы программы: {i}', end='\r', flush=True)
