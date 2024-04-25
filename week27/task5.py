glas = 'аеёиоуыэюя'
sign = 'ьъ'


def let_type(let):
    if let.lower() in glas:
        return 'Гласная'
    if let.lower() in sign:
        return 'Знак'
    return 'Согласная'


def print_letter(let, n):
    print(f'[{let.upper()}] [{let.lower()}]')
    print(f'{n}-я буква алфавита')
    print(let_type(let))


letters = ''.join(chr(i) if chr(i) != 'е' else 'её' for i in range(ord('а'), ord('я')+1))

print('-' * 19)
for n, i in enumerate(letters, 1):
    print_letter(i, n)
    print('-'*19)
