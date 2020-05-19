class Worker:
    def data(self, name, surname, income):
        self.name = name
        self.surname = surname
        self.__income = income


class Position(Worker):
    def get_full_name(self, name, surname):
        print(f'Сотрудник: {surname} {name}')

    def get_total_income(self, income):
        print(f'Зарплата с учётом премии составляет: {income.get("wage") + income.get("bonus")}')


pos_1 = Position()
pos_1.get_full_name(name=input('Введите имя сотрудника: '), surname=input('Введите фамилию сотрудника: '))
pos_1.get_total_income(income={"wage": float(input('Введите зарплату сотрудника: ')), \
                               "bonus": float(input('Введите премию сотрудника: '))})
