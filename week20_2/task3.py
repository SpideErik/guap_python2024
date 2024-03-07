def calc(s):
    for op in '+-*/':
        operand = s.split(op)
        if len(operand) != 2:
            continue
        for i in range(2):
            operand[i] = float(operand[i])
        if op == '+':
            return sum(operand)
        if op == '-':
            return operand[0] - operand[1]
        if op == '*':
            return operand[0] * operand[1]
        if op == '/':
            return operand[0] / operand[1]
    raise ValueError('Неверное количество операндов')


while s := input('Выражение>').replace(' ', '').replace(',', '.'):
    try:
        r = calc(s)
        print(f'{s} = {r}')
    except ValueError:
        print('Строка содержит недопустимое выражение')
