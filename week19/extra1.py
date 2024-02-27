from random import randint


def quick_sort(lst):
    if not lst:
        return lst
    pivot = lst.pop()
    start = list(filter(lambda x: x <= pivot, lst))
    stop = list(filter(lambda x: x > pivot, lst))
    return quick_sort(start) + [pivot] + quick_sort(stop)


data = [randint(1, 100) for i in range(20)]
print(data)
print(quick_sort(data))
