from random import shuffle


lst = list('ABCDEFGHIJ') + list(range(10))
print('Стартовый список')
print(lst)

shuffle(lst)
print('Перетасованный список')
print(lst)

pairs = [[lst[i], lst[i+1]] for i in range(0, len(lst), 2)]
print('Список готовый к конвертации в словарь')
print(pairs)

pairs = dict(pairs)
print('Словарь')
print(pairs)
