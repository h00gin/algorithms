#Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции
# дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def string(user_str):
    len_ = sum_ = 0
    unique = []
    while len_ < len(user_str):
        len_ += 1
        for i in range(len(user_str)):
            h_elem = hashlib.sha1(user_str[i:len_].encode('utf-8')).hexdigest()
            if h_elem not in unique and h_elem != hashlib.sha1(''.encode('utf-8')).hexdigest() \
                    and h_elem != hashlib.sha1(user_str.encode('utf-8')).hexdigest():
                unique.append(h_elem)
                sum_ += 1
    return f'Количество различных подстрок в строке "{user_str}": {sum_}'


print(string('papa'))
print(string('sova'))
