words = input('Введите несколько слов через пробел: ')
words = words.split( )
for index, elem in enumerate(words, 1):
    print(index, elem[:10])