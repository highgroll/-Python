from itertools import count, cycle

number = int(input('Введите количество элементов списка: '))
start_number = int(input('Введите значение первого элемента списка: '))
start = 0
new_start = 0
my_list = []
for el in count(start_number, number):
    new_start += 1
    my_list.append(el)
    if new_start >= number:
        break
print(my_list)
for el in cycle(my_list):
    start += 1
    print(el)
    if start >= number:
        break
