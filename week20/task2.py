from collections import Counter
from random import choices


names_init = ['Ян', 'Аня', 'Витя', 'Игорь', 'Богдан']

names = choices(names_init, k=50)
cnt = Counter(names)

print(cnt)
print(' '.join(cnt))
for key, val in cnt.items():
    s = str(val)
    s += ' '*(len(key) - len(s))
    print(s, end=' ')
