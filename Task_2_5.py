my_list = [9, 8, 7, 6, 5, 5, 4, 3, 2]
number = int(input('Введите новый элемент рейтинга: '))
for el in my_list:
    count_num = my_list.count(number)
    if number > el:
        next_index = my_list.index(el)
        my_list.insert(next_index, number)
        break
    elif count_num > 0:
        index = my_list.index(number)
        my_list.insert(index + count_num, number)
        break
    elif number < my_list[len(my_list) - 1]:
        my_list.append(number)
        break
print(my_list)