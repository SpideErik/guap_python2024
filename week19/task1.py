name_list = sorted(['Саша', 'Рома', 'Эрик', 'Игорь', 'Оля', 'Юра', 'Аня', 'Егор', 'Женя', 'Вова'])

names = {key: name for key, name in enumerate(name_list, 1)}
# names = {}
# for key, name in enumerate(name_list, 1):
#     names[key] = name

for key in names:
    print(f'{key}й в списке - {names[key]}')
