from random import choice

trigger = {
    'привет': ['Hello!', 'Привет!', 'Добрый день.'],
    'выход': ['Пока-пока!', 'Выключение...', 'Завершение работы'],
    'новости': ['Ничего нового!', 'Все идет по плану.', 'Новостей нет.'],
    'дела': ['Отлично!', 'Хорошо!', 'Лучше всех!'],
}


def run():
    while True:
        for word in input('>').lower().split():
            if word in trigger:
                print(choice(trigger[word]))
                if word == 'выход':
                    return
                break
        else:
            print('Я вас не понял!')


print('Программа запущена')
run()
print('Программа завершена')
