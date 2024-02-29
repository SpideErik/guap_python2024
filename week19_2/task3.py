name_list = ['Саша', 'Рома', 'Эрик', 'Игорь', 'Оля', 'Юра', 'Аня', 'Егор', 'Женя', 'Галя']
print(name_list)

letters = []
for name in name_list:
    letters.extend(name.lower())
letters.sort()
print(letters)

let_dict = {}
for let in letters:
    if let in let_dict:
        let_dict[let] += 1
    else:
        let_dict[let] = 1
print(let_dict)

let_list = [[i[1], i[0]] for i in let_dict.items()]
let_list.sort(reverse=True)
print(let_list)

print('Самые частые буквы')
for i in range(3):
    print(f'{i+1}-место буква {let_list[i][1]}, встречается {let_list[i][0]}')
