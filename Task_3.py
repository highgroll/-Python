num = str(input('Введите число: '))
double_num = ('{0}{1}'.format(num, num))
triple_num = ('{0}{1}{2}'.format(num, num, num))
print(int(num) + int(double_num) + int(triple_num))