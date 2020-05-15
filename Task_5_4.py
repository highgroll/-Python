import re

with open('text_4.txt', 'r', encoding='utf-8') as my_file:
    content = my_file.read()


    def clean_content(content):
        content = re.sub('One', 'Один', content)
        content = re.sub('Two', 'Два', content)
        content = re.sub('Three', 'Три', content)
        content = re.sub('Four', 'Четыре', content)
        content = re.sub('Five', 'Пять', content)
        content = re.sub('Six', 'Шесть', content)
        content = re.sub('Seven', 'Семь', content)
        content = re.sub('Eight', 'Восемь', content)
        content = re.sub('Nine', 'Девять', content)
        content = re.sub('Ten', 'Деять', content)
        return content


    new_content = clean_content(content)
    print(new_content)
with open('text_4_russian.txt', 'w', encoding='utf-8') as my_file:
    my_file.writelines(new_content)
    print(f'Ваши данные записаны в файл {my_file.name}')
