# Определить, какое число в массиве встречается чаще всего

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Заданный массив: {array}')

dict_num = {}
for i in array:
    if i in dict_num:
        dict_num[i] += 1
    else:
        dict_num[i] = 1
max_ = list(dict_num.values())[0]
max_id = list(dict_num.keys())[0]
for key, value in dict_num.items():
    if value > max_:
        max_ = value
        max_id = key
print(f'В заданном массиве чаще всего встречается число: {max_id}')








