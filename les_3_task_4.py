#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Заданный массив: {array}')

min_, max_ = array[0], array[0]
max_id, min_id = 0, 0
sum_num = 0
for i in range(len(array)):
    if array[i] < min_:
        min_ = array[i]
        min_id = i
    if array[i] > max_:
        max_ = array[i]
        max_id = i
for i in range(len(array)):
    if min_id < i < max_id or max_id < i < min_id:
        sum_num += array[i]
print(f'Минимальный элемент массива: {min_}\nМаксимальный элемент массива: {max_}')
print(f'Сумма элементов, находящихся между минимальным и максимальным элементами: {sum_num}')