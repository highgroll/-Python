my_list = list(input('Введите элементы списка: '))
print(my_list)
for el in range(1, len(my_list), 2):
    my_list[el - 1], my_list[el] = my_list[el], my_list[el - 1]
print(list(''.join(my_list)))


