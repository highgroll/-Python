class Road:
    def count(self, length, width, height):
        self.__length = length  # длинна дороги
        self.__width = width  # ширина дороги
        self.__height = height  # толщина дорожного покрытия
        print(f'Для покрытия всей дороги требуется: {length * width * height * 25 / 1000} тонн асфальта')


road_66 = Road()
road_66.count(length=int(input('Введите проектную проятижённость дороги в метрах: ')), \
              width=int(input('Введите проектную ширину дороги в метрах: ')), \
              height=int(input('Введите проектную толщину дороги в сантиметрах: ')))
