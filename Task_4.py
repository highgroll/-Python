num = int(input('Введите число: '))
digit = num % 10
num = num // 10
while num > 0:
    if num % 10 > digit:
        digit = num % 10
    num = num // 10
print(digit)