# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
# должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать
# скорость и сложность алгоритмов.

import timeit
import cProfile

MAX_SIM = 10000


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
            return b[k]


print(timeit.timeit('sieve_erato(2)', number=50, globals=globals())) #0.847435462
print(timeit.timeit('sieve_erato(4)', number=50, globals=globals())) #0.9022913419999999
print(timeit.timeit('sieve_erato(8)', number=50, globals=globals())) #0.826019337
print(timeit.timeit('sieve_erato(200)', number=50, globals=globals())) #0.8257893089999997
print(timeit.timeit('sieve_erato(1000)', number=50, globals=globals())) #0.8488615139999998

cProfile.run('sieve_erato(1000)')
#  7 function calls in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.017    0.017    0.021    0.021 les_4_task_2.py:12(sieve_erato)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:13(<listcomp>)
#         1    0.002    0.002    0.002    0.002 les_4_task_2.py:25(<listcomp>)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('*' * 50)


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
            return simple[k]


# print(timeit.timeit('not_sieve(2)', number=50, globals=globals())) #80.623706622
# print(timeit.timeit('not_sieve(4)', number=50, globals=globals())) #76.128372985
# print(timeit.timeit('not_sieve(8)', number=50, globals=globals())) #76.164881587
cProfile.run('not_sieve(1000)')

# 1234 function calls in 1.990 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.990    1.990 <string>:1(<module>)
#         1    1.989    1.989    1.990    1.990 les_4_task_2.py:32(not_sieve)
#         1    0.000    0.000    1.990    1.990 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1229    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('*' * 50)


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
                return i


print(timeit.timeit('simple_num(2)', number=50, globals=globals())) #0.00014308800000062405
print(timeit.timeit('simple_num(4)', number=50, globals=globals())) #0.00034534400000030274
print(timeit.timeit('simple_num(8)', number=50, globals=globals())) #0.0011054609999998632
print(timeit.timeit('simple_num(200)', number=50, globals=globals())) #1.0282795259999995
print(timeit.timeit('simple_num(1000)', number=50, globals=globals())) #44.589535729999994
cProfile.run('simple_num(1000)')
# 4 function calls in 1.102 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    1.102    1.102 <string>:1(<module>)
#         1    1.102    1.102    1.102    1.102 les_4_task_2.py:47(simple_num)
#         1    0.000    0.000    1.102    1.102 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('*' * 50)

# Считаю, что в данном случае вариант без решета Эратосфена и без создания массива для решения данной задачи наиболее
# оптимален лишь при небольшом объеме данных, так как время выполнения программы меньше (не затрачивается время на
# создание массива простых чисел и вывод значения индекса простого числа происходит в одном цикле). Однако, с большим
# объемом данных вариант с решетом Эратосфена работает заметно лучше, так как асимптотика линейная и время работы
# программы возрастает не значительно.






