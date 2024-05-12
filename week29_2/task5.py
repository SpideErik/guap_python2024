import re


while True:
    s = input('Введите пароль>')
    if re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?@#<>])[a-zA-Z0-9!?@#<>]{8,24}', s):
        print(f'{s} подходит')
        break
    print('Пароль не соответствует требованиям')
