import re


def calc(s):
    parts = re.split(r"([\+\-\*\/])", s)
    if len(parts) != 3:
        raise ValueError('Неверное количество операндов')
    try:
        operand = [float(parts[0]), float(parts[2])]
    except ValueError:
        raise ValueError('Операции только над числами')
    op = parts[1]

    if op == '+':
        return sum(operand)
    if op == '-':
        return operand[0] - operand[1]
    if op == '*':
        return operand[0] * operand[1]
    if op == '/':
        if operand[1] == 0:
            raise ValueError("деление на 0")
        return operand[0] / operand[1]


while s := input('Выражение>').replace(' ', '').replace(',', '.'):
    try:
        r = calc(s)
        print(f'{s} = {r}')
    except ValueError:
        print('Строка содержит недопустимое выражение')
