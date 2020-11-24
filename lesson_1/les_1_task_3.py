#Определить, является ли год, который ввел пользователь, високосным или не високосным.

print('Определение високосного года.')
year = int(input('Введите год: '))
check_four = year % 4
if check_four == 0:
    check_hundred = year % 100
    if check_hundred == 0:
        check_four_hundred = year % 400
        if check_four_hundred == 0:
            print(f'год {year} - високосный')
        else:
            print(f'год {year} - не високосный')
    else:
        print(f'год {year} - високосный')
else:
    print(f'год {year} - не високосный')
