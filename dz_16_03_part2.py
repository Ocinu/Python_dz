"""
Задание #1:
Создать класс "Компьютер" у которого должны быть следующие параметры:
 - Имя компьютера
 - Количество оперативной памяти
 - Мощность процессора (от 1 до 100)
"""


class Computer:
    def __init__(self, name, memory, proc):
        self.name = name
        self.memory = memory
        self.proc = proc


"""
Задание #2:
Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
"""


class Stadion:

    def __init__(self, name, date, city, country, width):
        self.name = name
        self.date = date
        self.city = city
        self.country = country
        self.width = width

    def __str__(self):
        print(f'{self.date}, {self.name}, {self.city}, {self.country}, {self.width}')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value: str):
        self._date = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value: str):
        self._country = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: str):
        self._width = value

    def get_place(self):
        print(f'{self.country}, {self.city}')

    def get_width(self):
        print(f'{self.width}, {self.name}')


"""
Задание #3:
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы.
"""


class Device:
    def __init__(self, total):
        self.total = total

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value


class CoffeeMachine(Device):
    def __init__(self, info, total):
        self.info = info
        super(CoffeeMachine, self).__init__(total)

    def __str__(self):
        return f'{self.total}, {self.info}'

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value


class Blender(Device):
    def __init__(self, info, total):
        self.info = info
        super(Blender, self).__init__(total)

    def __str__(self):
        return f'{self.total}, {self.info}'

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value


class MeatGrinder(Device):
    def __init__(self, info, total):
        self.info = info
        super(MeatGrinder, self).__init__(total)

    def __str__(self):
        return f'{self.total}, {self.info}'

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

