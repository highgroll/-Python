distance = float(input('Введите дистанцию за первй день тренировок, км.: '))
aim = int(input('Введите требуемую дистанцию, км.:  '))
count = 1
while distance <= aim:
    count += 1
    print('{:.2f}'.format(distance), 'км.')
    distance *= 1.1
print('{:.2f}'.format(distance), 'км.')
print('Требуемая дистанция достигнута на', count, '- й день тренировок')
