#Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.

SIZE_M = 5
SIZE_N = 3
matrix = [[int(input(f'Введите a{j+1}{i+1} элемент матрицы A: ')) for i in range(SIZE_N)] for j in range(SIZE_M)]
matrix_result = []
for el in matrix:
    matrix_result.append(el)
    sum_num = 0
    for i in el:
        sum_num += i
    el.append(sum_num)
print('\nПолученная матрица (последний столбец равен сумме элементов строки):')
print(*matrix_result, sep='\n')
