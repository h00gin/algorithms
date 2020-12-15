# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.

import timeit
import cProfile

# вариант 1. с рекурсией


def sum_num(a, n):
    if n == 1:
        return a
    else:
        return a + sum_num((-a / 2), (n - 1))


print(timeit.timeit('sum_num(1, 10)', number=100, globals=globals())) #0.0004842060000000009
print(timeit.timeit('sum_num(1, 50)', number=100, globals=globals())) #0.0025278909999999974
print(timeit.timeit('sum_num(1, 100)', number=100, globals=globals())) #0.005841256000000003
cProfile.run('sum_num(1, 900)')
# 903 function calls (4 primitive calls) in 0.002 seconds

   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
   #  900/1    0.002    0.000    0.002    0.002 les_4_task_1.py:10(sum_num)
   #      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('*' * 50)


# вариант 2. с циклом


def sum_cycle(a, n):
    sum_ = a
    for i in range(n - 1):
        if i % 2 != 0:
            b = a / (2 ** (i + 1))
            sum_ += b
        else:
            b = - (a / (2 ** (i + 1)))
            sum_ += b
    return sum_


print(timeit.timeit('sum_cycle(1, 10)', number=100, globals=globals())) #0.0011531580000000013
print(timeit.timeit('sum_cycle(1, 50)', number=100, globals=globals())) #0.007946522000000011
print(timeit.timeit('sum_cycle(1, 100)', number=100, globals=globals())) #0.018738506000000002
cProfile.run('sum_cycle(1, 900)')
# 4 function calls in 0.005 seconds

   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
   #      1    0.004    0.004    0.004    0.004 les_4_task_1.py:38(sum_cycle)
   #      1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
print('*' * 50)


# вариант 3. со встроенной функцией sum

def sum_sum(a, n):
    list_num = []
    for i in range(n - 1):
        if i % 2 != 0:
            b = a / (2 ** (i + 1))
            list_num.append(b)
        else:
            b = - (a / (2 ** (i + 1)))
            list_num.append(b)
    sum_ = sum(list_num)
    return sum_ + a


print(timeit.timeit('sum_sum(1, 10)', number=100, globals=globals())) #0.0009442610000000018
print(timeit.timeit('sum_sum(1, 50)', number=100, globals=globals())) #0.007488882000000002
print(timeit.timeit('sum_sum(1, 100)', number=100, globals=globals())) #0.023299817
cProfile.run('sum_sum(1, 900)')
#904 function calls in 0.008 seconds

   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.008    0.008 <string>:1(<module>)
   #      1    0.008    0.008    0.008    0.008 les_4_task_1.py:34(sum_sum)
   #      1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
   #    899    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print('*' * 50)

# Считаю, что в данном случае вариант c рекурсией наиболее оптимальным, так как суммарное время выполнения
# программы наименьшее и функция имеет линейный вид. Вариант с применением стандартной функции наменее оптимален,
# так как в данном случае происходит затрата времени на создания массива с заданной последовательностью
