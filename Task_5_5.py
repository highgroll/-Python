with open('my_text_5.txt', 'w', encoding='utf-8') as my_file:
    my_str = input('Введите список значений через пробел: ')
    my_file.write(my_str)
with open('my_text_5.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.read()
    content = content.split()
    result = 0
    for el in content:
        result = result + int(el)
print(result)
