"""
Задание:
1) Нужно создать абстрактный класс "Машина".
Который должен содержать следующие функции:
 - Получить марку
 - Получить год покупки машины
 - Получить цену
 - Получить пробег
"""


class Car:
    def __init__(self, mark, year, price, mileage):
        self.mark = mark
        self.year = year
        self.price = price
        self.mileage = mileage

    def get_mark(self):
        pass

    def get_year(self):
        pass

    def get_price(self):
        pass

    def get_mileage(self):
        pass


"""
2) Создать класс "BMW", "Audi", "Bentley" которые будут наследоваться от класса "Машина", они должны содержать полную 
реализацию всех функций класса от которого наследуются.
В качестве готового ДЗ отправить файл с расширением .py
"""


class BMW(Car):
    def __init__(self, mark, year, price, mileage):
        super(BMW, self).__init__(mark, year, price, mileage)

    def __str__(self):
        return f'{self.mark}, {self.year}, {self.price}, {self.mileage}'

    def __lt__(self, other):
        return self.price < other.price

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value: str):
        self._mark = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value: int):
        self._mileage = value

    def get_mark(self):
        return self.mark

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_mileage(self):
        return self.mileage

    def calc_high_mileage(self):
        if self.year == 2021:
            temp = self.mileage
        else:
            temp = self.mileage / (2021 - self.year)
        if temp >= 17000:
            return True
        else:
            return False


class Audi(Car):
    def __init__(self, mark, year, price, mileage):
        super(Audi, self).__init__(mark, year, price, mileage)

    def __str__(self):
        return f'{self.mark}, {self.year}, {self.price}, {self.mileage}'

    def __lt__(self, other):
        return self.price < other.price

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value: str):
        self._mark = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value: int):
        self._mileage = value

    def get_mark(self):
        return self.mark

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_mileage(self):
        return self.mileage

    def calc_high_mileage(self):
        if self.year == 2021:
            temp = self.mileage
        else:
            temp = self.mileage / (2021 - self.year)
        if temp >= 17000:
            return True
        else:
            return False


class Bentley(Car):
    def __init__(self, mark, year, price, mileage):
        super(Bentley, self).__init__(mark, year, price, mileage)

    def __str__(self):
        return f'{self.mark}, {self.year}, {self.price}, {self.mileage}'

    def __lt__(self, other):
        return self.price < other.price

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value: str):
        self._mark = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: int):
        self._price = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value: int):
        self._mileage = value

    def get_mark(self):
        return self.mark

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def get_mileage(self):
        return self.mileage

    def calc_high_mileage(self):
        if self.year == 2021:
            temp = self.mileage
        else:
            temp = self.mileage / (2021 - self.year)
        if temp >= 17000:
            return True
        else:
            return False
