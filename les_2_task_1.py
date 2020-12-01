#https://drive.google.com/file/d/12ccjekgokWaRsgMhk5aCEdQ7lFsQnXSf/view?usp=sharing

#Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = str(input('Введите целое число: '))
even, not_even = 0, 0
for i in a:
    i = int(i)
    if i % 2 == 0:
        even = even + 1
    else:
        not_even = not_even + 1
print(f'В заднном числе четных цифр - {even}, нечетных - {not_even}')