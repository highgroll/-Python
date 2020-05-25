number = input('Введите делимое: ')
denom = input('Введите делитель: ')
try:
    print(f'Частное от деления равно: {int(number / denom)}')
except ZeroDivisionError:
    print('Деление на ноль невозможно')
except TypeError:
    print('Деление невозможно, запустите программу ещё раз и введите корректные значения для делимого или делителя')
finally:
    print('Решение задачи завершено')
