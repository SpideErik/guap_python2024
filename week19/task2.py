from random import shuffle

name_list = sorted(['Саша', 'Рома', 'Эрик', 'Игорь', 'Оля', 'Юра', 'Аня', 'Егор', 'Женя', 'Вова'])

numbers = list(range(1, 11))
shuffle(numbers)

print(name_list)
print(numbers)

name_num = list(zip(numbers, name_list))
print(name_num)

name_num.sort()
print(name_num)

names = {key: name for key, name in name_num}
# names = {}
# for key, name in name_num:
#     names[key] = name

print(names)
