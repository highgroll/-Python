import re

with open('text_6.txt', 'r', encoding='utf-8') as my_file:
    content_list = {}
    while True:
        content = my_file.readline()
        if len(content) == 0:
            break


        def clean_content(content):
            content = re.sub('[%s]' % re.escape("""(),-:"""), '', content)
            content = re.sub('([а-я])', '', content)
            content = re.sub('\s+', ' ', content)
            return content


        content = re.findall('\w*', clean_content(content))
        summa = 0
        for index in range(1, len(content)):
            if content[index] != '':
                summa = summa + int(content[index])
        my_dict = {content[0]: summa}
        content_list.update(my_dict)
    print(content_list)
