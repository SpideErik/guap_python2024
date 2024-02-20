from random import randint, choice

name_list = ['Саша', 'Рома', 'Эрик', 'Игорь', 'Оля', 'Юра']
s_names_list = ['Иванов(а)', 'Петров(а)', 'Сидоров(а)', 'Лебедев(а)', 'Гусев(а)']
n = int(input('Кол-во студентов>'))

students = []
for i in range(1, n+1):
    student = [choice(name_list), choice(s_names_list), randint(2010, 2023)]
    if student[2] > 2018:
        student.append(f'{2024 - student[2]}й курс')
    else:
        student.append(f'Выпустился в {student[2]+5}')
    students.append(student)
    print(f'{i}-{student}')
