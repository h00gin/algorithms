# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merger(arr):
    half = int(len(arr) / 2)
    if len(arr) <= 1:
        return arr
    else:
        arr_1 = arr[:half]
        arr_2 = arr[half:]
        return sort(merger(arr_1), merger(arr_2))


def sort(arr_1, arr_2):
    result = []
    i, j = 0, 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            result.append(arr_1[i])
            i += 1
        else:
            result.append(arr_2[j])
            j += 1
    result += arr_1[i:] + arr_2[j:]
    return result


array = [round(random.uniform(0, 50), 2) for i in range(10)]
print(f'Исходный массив: {array}')
print(f'Отсортированный массив: {merger(array)}')

