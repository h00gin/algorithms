# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в
# рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

import sys, platform

MAX_SIM = 10000


# функция подсчета занимаемой памяти
def mem_count(*args):
    sum_ = 0
    for elem in args:
        sum_ += sys.getsizeof(elem)
    return f'Общий объем занимаемой памяти: {sum_} байт'


# 1. c решетом Эратосфена
def sieve_erato(count):
    a = [i for i in range(MAX_SIM)]
    a[1] = 0
    m = 2
    k = 0
    while m < MAX_SIM:
        if a[m] != 0:
            j = m * 2
            while j < MAX_SIM:
                a[j] = 0
                j = j + m
                k += 1
        m += 1
    b = [i for i in a if a[i] != 0]
    for k in range(len(b)):
        if count == k + 1:
            return f'Вариант 1. Ответ: {b[k]}', mem_count(a, a[1], m, k, MAX_SIM, j, b, count)


# 2. без решета Эратосфена (с массивом)
def not_sieve(count):
    k = 0
    simple = []
    for i in range(2, MAX_SIM):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            simple.append(i)
    for k in range(len(simple)):
        if count == k + 1:
            return f'Вариант 2. Ответ: {simple[k]}', mem_count(count, k, simple, i, MAX_SIM, j)


# 3. без решета Эратосфена (без массива)
def simple_num(count):
    k = 0
    for i in range(2, MAX_SIM):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            k += 1
            if count == k:
                return f'Вариант 3. Ответ: {i}', mem_count(count, k, i, MAX_SIM, j)


print(sieve_erato(100))
print(not_sieve(100))
print(simple_num(100))
print(f'Версия Python: {sys.version_info.major}.{sys.version_info.minor}')
print(f'Операционная система: {platform.architecture()}')

# ('Вариант 1. Ответ: 541', 'Общий объем занимаемой памяти: 48986 байт')
# ('Вариант 2. Ответ: 541', 'Общий объем занимаемой памяти: 5166 байт')
# ('Вариант 3. Ответ: 541', 'Общий объем занимаемой памяти: 70 байт')
# Версия Python: 3.8
# Операционная система: ('32bit', 'WindowsPE')

# В данной задаче наиболее затратной по объему занимаемой памяти является вариант с решетом Эратосфена, так как
# для использования решета в начале создается массив целых чисел и идет перебор каждого элемента. Наименее
# затратной является задача без решета и без создания массива, что и дает преимущество, так как в памяти не
# хранится объемный массив целых чисел и при нахождении нужного элемента перебор элементов массива прекращается