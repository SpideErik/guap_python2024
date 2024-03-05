from random import randint
from collections import Counter


n = 3 # кол-во строк

nums = [[] for _ in range(n)]

while all(sum(i) < 1000 for i in nums):
    for i in nums:
        i.append(randint(1, 20))

for n, i in enumerate(nums, 1):
    print(f'Самые частые значения в списке {n}: {Counter(i).most_common(3)}')
    print(f'Сумма значений {sum(i)}')
    print('Список:', i)
