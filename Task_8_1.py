class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'Дата: {self.day}-{self.month}-{self.year}'

    @classmethod
    def Data_by_int(cls, day, month, year):
        my_list = [day, month, year]
        result_list = []
        for el in my_list:
            el = int(el)
            result_list.append(el)
        return result_list

    @staticmethod
    def Check(day, month, year):
        if day < 0 and day > 31:
            return f'Введите корректное значения для дня'
        elif month < 0 and month > 12:
            return f'Введите корректное значения для месяца'
        elif year < 0 and year > 10000:
            return f'Введите корректное значения для года'
        else:
            return f'Дата верная'


data_1 = Data(5, 5, 2010)
print(data_1)
print(data_1.Check(5, 5, 2010))
print(data_1.Data_by_int(5, 5, 2010))
