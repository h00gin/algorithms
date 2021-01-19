# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве
# медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.

import random

RED_FACT = 1.247

# сортировка расческой


def comb(arr):
    dist = len(arr)
    while dist > 1:
        if dist > 1:
            dist = int(dist / RED_FACT)
        for i in range(len(arr) - dist):
            if arr[i] > arr[i + dist]:
                arr[i], arr[i + dist] = arr[i + dist], arr[i]
    return arr


def median(arr):
    if len(arr) % 2 != 0:
        middle = int(len(arr) / 2 + 0.5) - 1
        return f'Медиана массива: {arr[middle]}'
    else:
        middle_right = int(len(arr) / 2)
        middle_left = int(len(arr) / 2) - 1
        return f'Медиана массива: {(arr[middle_right] + arr[middle_left]) / 2}'


m = int(input('Введите натуральное число m для определения длинны массива (2m + 1): '))
array = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив: {array}')
arr_sort = comb(array)
print(f'Отсортированный массив: {arr_sort}')
print(f'{median(arr_sort)}')
