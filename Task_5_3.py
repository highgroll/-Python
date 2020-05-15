with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    content_list = []
    new_list = []
    while True:
        content = (my_file.readline()).strip('\n')
        if len(content) == 0:
            break
        content_list.append(content.split())
    print('Список работников с зарплатой меньше 20000 руб:')
    ev_sal = 0
    index = 0
    for el in content_list:
        ev_sal = ev_sal + float(el[1])
        index += 1
        if float(el[1]) < 20000.0:
            print(f'{el[0]}: {el[1]}')
    print(f'Средняя зарплата всех работников составляет: {float(ev_sal / index)}')
