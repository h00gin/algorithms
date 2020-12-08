#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Заданный массив: {array}')

min_, max_ = array[0], array[0]
max_id, min_id = 0, 0
for i in range(len(array)):
    if array[i] < min_:
        min_ = array[i]
        min_id = i
    if array[i] > max_:
        max_ = array[i]
        max_id = i
array[min_id], array[max_id] = array[max_id], array[min_id]
print(f'Минимальный элемент массива: {min_}\nМаксимальный элемент массива: {max_}')
print(f'Получившийся массив: {array}')