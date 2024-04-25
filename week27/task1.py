def yesno():
    while True:
        s = input('Продолжать?')
        if s.lower() in ('да', 'yes'):
            return True
        if s.lower() in ('нет', 'no'):
            return False


answer = True
while answer:
    s1 = input('Введите строку>')
    s2 = input('Введите подстроку>')
    if s1.lower().find(s2.lower()):
        print('Совпадение найдено')
    else:
        print('Совпадений нет')
    answer = yesno()
