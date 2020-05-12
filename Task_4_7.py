from math import factorial

num = int(input('Введите число: '))


def fact(num):
    for el in range(1, num + 1):
        yield el


for el in fact(num):
    print(f'{el}! = {factorial(el)}')
