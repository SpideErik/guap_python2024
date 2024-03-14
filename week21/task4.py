from pathlib import Path

fn = Path('data.txt')


def write_data():
    s = input('Введите строку>')
    with fn.open('at', encoding='UTF8') as f:
        print(s, file=f)


def read_text():
    try:
        print(fn.read_text(encoding='UTF8'))
    except FileNotFoundError:
        print('Файл еще не создан')


def read_line():
    try:
        lines = fn.read_text(encoding='UTF8').splitlines()
    except FileNotFoundError:
        print('Файл еще не создан')
        return

    try:
        n = int(input('Введите номер строки>'))
    except ValueError:
        n = 0
    n -= 1
    if 0 < n < len(lines):
        print(lines[n])
    else:
        print('Неверный номер строки')


def exit_prg():
    print('Завершение работы')
    exit()


commands = {
    '1': ['Запись данных', write_data],
    '2': ['Чтение документа', read_text],
    '3': ['Чтение строки', read_line],
    '4': ['Выход из программы', exit_prg]
}


def menu():
    while True:
        print('Команды управления')
        for key, v in commands.items():
            print(f'    {key}-{v[0]}')
        n = input('Выбор>')
        if n in commands:
            return n
        print('Неверная команда')


while True:
    cmd = menu()
    commands[cmd][1]()
