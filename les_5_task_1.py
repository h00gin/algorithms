#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Company = namedtuple('Company', 'name, profit_1, profit_2, profit_3, profit_4')
quantity = int(input('Введите количество предприятий: '))
profit_sum = 0
list_comp = []
for i in range(quantity):
    comp = Company(name=input('Введите название предприятия: '),
                   profit_1=int(input('Введите прибыль за 1й квартал: ')),
                   profit_2=int(input('Введите прибыль за 2й квартал: ')),
                   profit_3=int(input('Введите прибыль за 3й квартал: ')),
                   profit_4=int(input('Введите прибыль за 4й квартал: ')))
    list_comp.append(comp)
    profit_sum += comp.profit_1 + comp.profit_2 + comp.profit_3 + comp.profit_4
avg = round((profit_sum/quantity), 2)
print(f'Средняя прибыль всех предприятий за год: {avg}')
comp_plus = []
comp_minus = []
for comp in list_comp:
    prof_comp = 0
    prof_comp += comp.profit_1 + comp.profit_2 + comp.profit_3 + comp.profit_4
    if prof_comp > avg:
        comp_plus.append(comp.name)
    else:
        comp_minus.append(comp.name)
print(f'Предприятия с прибылью выше среднего: {comp_plus}')
print(f'Предприятия с прибылью ниже среднего: {comp_minus}')