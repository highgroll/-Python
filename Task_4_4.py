from random import randrange

start_list = []
for index in range(20):
    start_list.append(randrange(100))
print(start_list)
# start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11] <- для контрольного теста
gen = (el for el in start_list if start_list.count(el) == 1)
result_list = [el for el in gen]
print(result_list)
