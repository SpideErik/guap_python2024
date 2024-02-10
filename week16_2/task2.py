import time
import msvcrt


def progress(cur, total):
    s = '[' + '#'*cur + '-'*(total-cur) + ']'
    print(s, end='\r', flush=True)


p1 = '1'
p2 = '2'
while p1 != p2:
    p1 = input('Введите новый пароль>')
    p2 = input('Подтвердите пароль>')
    print('Идет проверка пароля. Ожидайте.')
    progress(0, 10)
    for i in range(10):
        time.sleep(0.3)
        progress(i+1, 10)
    print()
    if p1 == p2:
        print('Пароль принят.')
    else:
        print('Пароли не совпадают.')
    print('Для продолжения нажмите любую клавишу')
    msvcrt.getch()
