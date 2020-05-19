import time


class TrafficLight:
    def running(self, color):
        self.__color = color
        while True:
            for el in ['Red', 'Yellow', 'Green', 'Yellow']:
                print(el)
                if el == 'Red':
                    time.sleep(7)
                elif el == 'Yellow':
                    time.sleep(2)
                elif el == 'Green':
                    time.sleep(9)


tlc = TrafficLight()
tlc.running(color=['Red', 'Yellow', 'Yellow', 'Green'])
time.sleep(3)
