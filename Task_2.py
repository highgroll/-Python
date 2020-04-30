time_sec = int(input("Введите время в секундах: "))

hours = time_sec // 3600
minutes = (time_sec - (hours * 3600)) // 60
seconds = (time_sec - (hours * 3600)) - (minutes * 60)
print("{:02}:{:02}:{:02}".format(hours, minutes, seconds))

