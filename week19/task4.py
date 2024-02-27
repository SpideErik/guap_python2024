from random import randint
name_list = ['Иванов Саша', 'Петров Рома', 'Сидоров Эрик', 'Пупкин Игорь', 'Лаврова Оля', 'Козлов Юра']
lessons = ['Математика', 'Физика', 'Химия', 'География']


def gen_grades():
    n = randint(5, 10)
    return [randint(2, 5) for _ in range(n)]


def make_log():
    log = {}
    for key in name_list:
        log[key] = {n: gen_grades() for n in lessons}
    return log


def calc_avg(entry):
    total = 0
    for key in entry:
        avg = round(sum(entry[key])/len(entry[key]))
        total += avg
        print(f'\tСредний балл по {key} = {avg}')
    print(f'Средний балл {round(total/len(entry))}')


log = make_log()
for key in log:
    print(key)
    for lesson in log[key]:
        print(f'Оценки по {lesson}: {log[key][lesson]}')
    calc_avg(log[key])
