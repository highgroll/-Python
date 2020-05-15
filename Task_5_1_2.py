# Решение задачи №1
with open('my_text.txt', 'w', encoding='utf-8') as my_file:
    my_list = []
    while True:
        data = input("Внесите данные: ")
        if len(data) < 1:
            break
        content = data + '\n'
        my_list.append(content)
    my_file.writelines(my_list)
print('Ответ на задачу №1')
print(f'Ваши данные записаны в файл {my_file.name}')
print(' ')
# Решение задачи №2
with open('my_text.txt', "r", encoding='utf-8') as my_file:
    content = my_file.readlines()
    print("Ответ на задачу №2")
    print(f'Количество строк в файле {my_file.name}: {len(content)}')
    for index, el in enumerate(content, 1):
        print(f'Количество слов в строке {index}: {len(el.split())}')
