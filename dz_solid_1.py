"""
Задача:
Создать классы для трех видов апартаментов.
Квартира с балконом, квартира без балкона,
частный дом, дом с басейном, при этом у всех
апартаментов есть свой конекретный адрес.
В любоые  апартаменты можно зайти и можно
выйти. Так же их можно открывать и закрывать.
К тому же у частных домов может быть в
наличии гараж. Реализовать данную программу
используя принципы S, O.
"""


class HouseShape:
    def __init__(self, address):
        self.address = address
        self.enter = True
        self.exit = True

    def open(self):
        return self.open

    def close(self):
        return self.close


class Apartment(HouseShape):
    def __init__(self, address):
        super(HouseShape).__init__(address)
        self.type = 'apartment'
        self.balcony = None

    def set_balcony(self, value):
        self.balcony = value
        return self.balcony


class House(HouseShape):
    def __init__(self, address, garage):
        super(HouseShape).__init__(address)
        self.type = 'house'
        self.garage = garage
        self.pool = None

    @property
    def garage(self):
        return self._garage

    @garage.setter
    def garage(self, value):
        self._garage = value

    def set_pool(self, value):
        self.pool = value
        return self.pool
