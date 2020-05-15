import json

with open('text_7.txt', 'r', encoding='utf-8') as my_file:
    firm_list = []
    index = 0
    summa = 0
    while True:
        content = my_file.readline()
        if len(content) == 0:
            break
        content = content.split()
        for el in content:
            profit = int(content[2]) - int(content[3])
            my_dict = {content[0]: profit}
            if profit > 0:
                index += 1
                summa = summa + profit
            av_profit = summa / index
            prf_dict = {'Average profit': av_profit}
        firm_list.append(my_dict)
    firm_list.append(prf_dict)
    print(firm_list)
    with open("my_file_7.json", "w") as write_f:
        json.dump(firm_list, write_f)
        print(f'Ваши данные записаны в файл {write_f.name}')
