class Car:
    def data(self, name, color, speed, direction, is_police):
        self.name = name
        self.is_police = is_police
        self.color = color
        self.speed = speed
        self.direction = direction

    def go(self, name, is_police, color, speed):
        return print(f'{name} {color} {is_police} поехала со скоростью {speed}')

    def stop(self, name, is_police, color):
        return print(f'{name} {color} {is_police} остановилась')

    def turn_direction(self, name, is_police, color, speed, direction):
        return print(f'{name} {color} {is_police} повернула на {direction} со скоростью {speed}')


class TownCar(Car):
    def show_speed(self, name, speed):
        if speed > 60:
            print(f'Скорость {speed} - превышен лимит скорости')
        return print(f'Скорость {speed}')


class SportCar(Car):
    is_police = False

    def show_speed(self, name, speed):
        return print(f'Скорость {speed}')


class WorkCar(Car):
    is_police = False

    def show_speed(self, name, speed):
        if speed > 40:
            return print(f'Скорость {speed} - превышен лимит скорости')


class PoliceCar(Car):
    def show_speed(self, name, speed):
        return print(f'Скорость {speed}')

    is_police = True


car_1 = PoliceCar()
car_1.go('WV', True, 'Голубая', 80)
car_1.turn_direction('WV', True, 'Голубая', 80, 'Направо')
car_1.show_speed('WV', 80)
car_1.stop('WV', True, 'Голубая')

car_2 = WorkCar()
car_2.go('Камаз', False, 'Серый', 80)
car_2.turn_direction('Камаз', False, 'Серый', 80, 'Направо')
car_2.show_speed('Камаз', 80)
car_2.stop('Камаз', False, 'Серый')

car_3 = TownCar()
car_3.go('Smart', False, 'Белый', 60)
car_3.turn_direction('Smart', False, 'Белый', 60, 'Налево')
car_3.show_speed('Smart', 60)
car_3.stop('Smart', False, 'Белый')

car_4 = SportCar()
car_4.go('Ferrari', False, 'Красный', 160)
car_4.turn_direction('Ferrari', False, 'Красный', 160, 'Направо')
car_4.show_speed('Ferrari', 160)
car_4.stop('Ferrari', False, 'Красный')
