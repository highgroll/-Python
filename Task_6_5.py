class Stationery:
    title = None

    def draw(self, title):
        print('Запуск отрисовки')


class Pen(Stationery):
    color = 'синий'

    def draw(self, title, color):
        print(f'Запуск отрисовки: {title}, цвет {color}')


class Pencil(Stationery):
    color = 'серый'

    def draw(self, title, color):
        print(f'Запуск отрисовки: {title}, цвет {color}')


class Handle(Stationery):
    color = 'красный'

    def draw(self, title, color):
        print(f'Запуск отрисовки: {title}, цвет {color}')


unit_1 = Pen()
unit_1.draw('шариковая ручка', 'синий')
unit_2 = Pencil()
unit_2.draw('простой карандаш', 'серый')
unit_3 = Handle()
unit_3.draw('маркер', 'красный')
