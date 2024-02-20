words = []
double = [[], []]

while True:
    word = input('Введите слово>').replace(' ', '')
    if not word:
        break
    words.append(word)
    print(f'{word} добавлено!')

for word in words:
    for i, letter in enumerate(word[:-1]):
        if letter == word[i+1]:
            double[0].append(word)
            break
    else:
        double[1].append(word)

print(words)

print(double)
