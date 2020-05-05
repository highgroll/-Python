my_list = []
index = 0
while True:
    index += 1
    if index > 3:
        break
    name = input('Внесите название товара: ')
    price = float(input('Внесите цену товара: '))
    amount = int(input('Внесите количество товара: '))
    good = {'название': name, 'цена': price, 'количество': amount, 'ед': 'шт'}
    catalog = (index, good)
    my_list.append(catalog)
print(my_list)
names = []
prices = []
amounts = []
catalog_keys = []
for catalog in my_list:
    for el in catalog:
        if type(el) == dict:
            names.append(el.get('название'))
            prices.append(el.get('цена'))
            amounts.append(el.get('количество'))
data = {'название': names, 'цена': prices, 'количество': amounts}
print(data)







