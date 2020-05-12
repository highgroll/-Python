gen = (el for el in range(20, 240))
result_list = [el for el in gen if el % 20 == 0 or el % 21 == 0]
print(result_list)
