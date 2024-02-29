names = {1: 'Саша', 2: 'Рома', 3: 'Эрик', 4: 'Игорь', 5: 'Оля', 6: 'Юра', 7: 'Аня', 8: 'Егор', 9: 'Женя', 10: 'Вова'}
print(names)

#  т.к. нельзя изменять словарь в цикле если он используется как итератор
#  будем запускать итерацию заново при каждом удалении
# while True:
#     for i in names:
#         if i % 2 == 0:
#             val = names.pop(i)
#             print(f'Запись удалена: {i} - {val}.')
#             break
#     else:
#         break

for i in tuple(names.keys()):
    if i % 2 == 0:
        val = names.pop(i)
        print(f'Запись удалена: {i} - {val}.')


print(names)
