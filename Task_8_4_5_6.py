class OfficeTech:
    pass


class Printer(OfficeTech):
    def __init__(self, printer_count, printer_dep, printer_new):
        self.printer_count = int(printer_count)
        self.printer_dep = int(printer_dep)
        self.printer_new = int(printer_new)

    def printer_quantity(self):
        p_stock = self.printer_count - self.printer_dep
        if p_stock < 0:
            return f'Невозможно передать {self.printer_dep} принтеров, на складе {self.printer_count} шт.\'' \
                   f'Будут переданы все имеющтеся в наличии'

        else:
            return f'В другие подразделения передано {self.printer_dep} принтеров. Остаток на складе {p_stock} принтеров'

    def printer_stock(self):
        if self.printer_count - self.printer_dep < 0:
            p_stock = self.printer_new
        else:
            p_stock = self.printer_count - self.printer_dep + self.printer_new
        return f'На склад добавлено {self.printer_new} принтеров. Остаток на складе {p_stock} принтеров'


class Scan(OfficeTech):
    def __init__(self, scan_count, scan_dep, scan_new):
        self.scan_count = int(scan_count)
        self.scan_dep = int(scan_dep)
        self.scan_new = int(scan_new)

    def scan_quantity(self):
        s_stock = self.scan_count - self.scan_dep
        if s_stock < 0:
            return f'Невозможно передать {self.scan_dep} сканеров, на складе {self.scan_count} шт.\'' \
                   f'Будут переданы все имеющиеся в наличии'
        else:
            return f'В другие подразделения передано {self.scan_dep} сканеров. Остаток на складе {s_stock} сканеров'

    def scan_stock(self):
        if self.scan_count - self.scan_dep < 0:
            s_stock = self.scan_new
        else:
            s_stock = self.scan_count - self.scan_dep + self.scan_new
        return f'На склад добавлено {self.scan_new} сканеров. Остаток на складе {s_stock} сканеров'


class Xerox(OfficeTech):
    def __init__(self, xerox_count, xerox_dep, xerox_new):
        self.xerox_count = int(xerox_count)
        self.xerox_dep = int(xerox_dep)
        self.xerox_new = int(xerox_new)

    def xerox_quantity(self):
        x_stock = self.xerox_count - self.xerox_dep
        if x_stock < 0:
            return f'Невозможно передать {self.xerox_dep} ксероксов, на складе {self.xerox_count} шт.\'' \
                   f'Будут переданы все имеющиеся в наличии'
        else:
            return f'В другие подразделения передано {self.xerox_dep} ксероксов. Остаток на складе {x_stock} ксероксов'

    def xerox_stock(self):
        if self.xerox_count - self.xerox_dep < 0:
            x_stock = self.xerox_new
        else:
            x_stock = self.xerox_count - self.xerox_dep + self.xerox_new
        return f'На склад добавлено {self.xerox_new} ксероксов. Остаток на складе {x_stock} ксероксов'


try:
    printers = Printer(input('Внесите количество принтеров на складе: '), \
                       input('Внесите количество принтеров для передачи в другие подразделения: '), \
                       input('Внесите количество принтеров поступивших на склад: '))
    scans = Scan(input('Внесите количество сканеров на складе: '), \
                 input('Внесите количество сканеров для передачи в другие подразделения: '), \
                 input('Внесите количество сканеров поступивших на склад: '))
    xeroxs = Xerox(input('Внесите количество ксероксов на складе: '), \
                   input('Внесите количество ксероксов для передачи в другие подразделения: '), \
                   input('Внесите количество ксероксов поступивших на склад: '))
except ValueError:
    print('Допустимы только целые числа')
try:
    print(printers.printer_quantity())
    print(printers.printer_stock())

    print(scans.scan_quantity())
    print(scans.scan_stock())

    print(xeroxs.xerox_quantity())
    print(xeroxs.xerox_stock())
except NameError:
    print('Допустимы только целые числа')
