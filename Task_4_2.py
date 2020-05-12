from random import randrange

start_list = []
for index in range(10):
    start_list.append(randrange(100))
print(start_list)
gen = (start_list[index] for index in range(1, len(start_list)) if start_list[index - 1] < start_list[index])
result_list = [el for el in gen]
print(result_list)
