def ask_name():
    while True:
        name = input('Введите имя>')
        if len(name) <= 10 and name.isalpha() and name[0].isupper() and name[1:].islower():
            return name
        print('Имя введено неверно.')


def ask_age():
    while True:
        try:
            age = int(input('Введите возраст>'))
        except ValueError:
            age = 0
        if 10 <= age <= 100:
            return age
        print('Возраст введен неверно')


name = ask_name()
age = ask_age()
print(f'Имя - {name}, возраст - {age}')
