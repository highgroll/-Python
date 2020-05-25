class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    numbers = input("Введите несколько целых чисел через проблел, для завершения наберите Stop: ")
    my_list = numbers.split()
    res_list = []
    try:
        if my_list.count("Stop") > 0:
            break
        for el in my_list:
            el = int(el)
            if type(el) == str:
                raise MyError('Вводить можно только числа')
            else:
                res_list.append(el)
    except ValueError:
        print('Вводить можно только числа')
    except MyError as err:
        print(err)
    else:
        print(res_list)
