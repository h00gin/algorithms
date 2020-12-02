# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры.

def sum_num(a, n):
    if n == 1:
        return a
    else:
        return a + sum_num((-a / 2), (n-1))


num_first = int(input('Введите 1й элемент ряда: '))
quantity = int(input('Введите количество элементов ряда: '))
b = sum_num(num_first, quantity)
print(b)
