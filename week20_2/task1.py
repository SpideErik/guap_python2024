ban_list = []
while word := input('Введите запрещенное слово>'):
    ban_list.append(word.lower())
    print(f'{word} - добавлено')
print('Запрещенные слова:', ban_list, sep='\n')

s = input('Предложение>')
if len(s) <= 10:
    raise ValueError('Слишком короткое предложение')

words = s.split()
for i, word in enumerate(words):
    if word.lower() in ban_list:
        words[i] = 'пииииюююю'

print(' '.join(words))
