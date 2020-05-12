from sys import argv

script_name, production, rate, premium = argv

print('Имя файла:', script_name)
print('Зарплата составляет: ', int(production) * int(rate) + int(premium), 'руб.')
