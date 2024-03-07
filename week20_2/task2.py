from collections import Counter


alpha = "".join(chr(i) if i != ord('е') else 'её' for i in range(ord('а'), ord('я')+1))


s = input('Введите строку>').replace(' ', '')
for let in s:
    if let not in alpha:
        raise ValueError('строка состоит не только из русских букв')

cnt = Counter(s)

for let, n in cnt.items():
    if n < 2:
        continue
    print(f'Буква "{let}" встречается - {n} раз, в алфавите под номером {alpha.index(let)+1}')
