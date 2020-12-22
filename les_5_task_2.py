# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from collections import deque

dict_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
           '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
           'c': 12, 'd': 13, 'e': 14, 'f': 15}
MAX_16 = 16


def rank(num_a, num_b):
    i = 0
    while i < abs((len(num_a) - len(num_b))):
        if len(num_a) > len(num_b):
            num_b.appendleft('0')
        else:
            num_a.appendleft('0')
    return num_a, num_b


# сложение чисел
def sum_16(num_a, num_b):
    sum_list = deque()
    for i, j in zip(num_a, num_b):
        sum_ = 0
        for key, value in dict_16.items():
            if i == key or j == key:
                if i != j:
                    sum_ += value
                else:
                    sum_ += 2 * value
        sum_list.appendleft(sum_)
    for k in range(len(sum_list) - 1):
        if sum_list[k] >= MAX_16:
            sum_list[k] -= MAX_16
            sum_list[k + 1] += 1
            if sum_list[-1] >= MAX_16:
                num = 1
                sum_list[-1] -= MAX_16
                sum_list.append(num)
    sum_list.reverse()
    for i in range(len(sum_list)):
        for key, value in dict_16.items():
            if sum_list[i] == value:
                sum_list[i] = key
    return sum_list


# Вводим числа в шестнадцатиречной системе (идеальный пользователь)
a = deque(input('Введите 1е число: '))
b = deque(input('Введите 2е число: '))
print(f'Первое число:{a}')
print(f'Второе число:{b}')
rank(a, b)
print(f'Сумма чисел:{sum_16(a, b)}')






