from random import randint


def ask_payload():
    while True:
        try:
            payload = int(input('Введите грузоподъемность>'))
        except ValueError:
            payload = 0
        if 100 <= payload <= 600:
            return payload
        print('грузоподъемность введена неверно')


def make_load(payload):
    return [randint(payload//10, payload//4) for _ in range(20)]


def upload(load, payload):
    truck = []
    current = 0
    while True:
        for i in load:
            if current + i <= payload:
                break
        else:
            return truck
        current += i
        truck.append(i)
        load.remove(i)


payload = ask_payload()
print(f'За рейс можно увезти до {payload} кг')

load = make_load(payload)
print(f'Список грузов: {load}')

race = []
while load:
    race.append(upload(load, payload))

print(f'Для перевозки нужно {len(race)} рейсов ')
for n, truck in enumerate(race, 1):
    print(f'Рейс {n}: масса: {sum(truck)}, грузы: {truck}')

