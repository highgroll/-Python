from functools import reduce

start_list = [el for el in range(100, 1001) if el % 2 == 0]


def sum_func(el, next_el):
    return el + next_el


print(start_list)
print('Сумма элементов списка =', reduce(sum_func, start_list))
