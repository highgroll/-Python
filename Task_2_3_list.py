my_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень','Зима']
month = int(input('Введите порядковый номер месяца: '))
for number, el in enumerate(my_list, 1):
    if number == month:
        print(el)




