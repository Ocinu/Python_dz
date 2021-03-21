"""
Задание:
Написать консольный интерфейс который должен реализовать следующие функции:
 - Добавление машины (Перед этим необходимо запросить марку "BMW", "Audi", "Bentley")
 - Удаление машины
 - Изменение машины
 - Просмотр всех машин (Реализовать с помощью функции __str__ во всех классах)
 - Посмотреть машины с большым пробегом (Большой пробег считается если машина за год проехала больше 17К км.
Например машину купили в 2019 году, а ее пробег составляет 60К, допустимой нормой за год 17К,
машина проездила уже +2 года (2021-2019), т.е. нормальный пробег для нее составляет 34К км)
 - Получить 5 машин с самой большой/маленькой ценой

!!Нужно использовать код из первого задания.

В качестве готового ДЗ отправить файл с расширением .py

https://github.com/Ocinu/Python_dz/blob/main/dz_12_03_part2.py
"""
from dz_12_03 import *


class Carmarket:
    def __init__(self):
        self.car_storage = []

    def create_bmw(self):
        bmw = BMW(self.set_mark(), self.set_year(), self.set_price(), self.set_mileage())
        self.car_storage.append(bmw)

    def create_audi(self):
        audi = Audi(self.set_mark(), self.set_year(), self.set_price(), self.set_mileage())
        self.car_storage.append(audi)

    def create_bentley(self):
        bentley = Bentley(self.set_mark(), self.set_year(), self.set_price(), self.set_mileage())
        self.car_storage.append(bentley)

    @staticmethod
    def set_mark():
        while True:
            value = input('Введите марку машины')
            if isinstance(value, str):
                return value

    @staticmethod
    def set_year():
        while True:
            try:
                value = int(input('Введите год выпуска 1900 - 2021'))
                if 1900 <= value <= 2021:
                    return value
            except:
                print('Ошибка ввода')

    @staticmethod
    def set_price():
        while True:
            try:
                value = float(input('Введите цену машины'))
                return value
            except:
                print('Ошибка ввода')

    @staticmethod
    def set_mileage():
        while True:
            try:
                value = int(input('Введите пробег'))
                return value
            except:
                print('Ошибка ввода')

    def get_all_cars(self):
        for idx, i in enumerate(self.car_storage):
            print(f'{idx} - {i}')

    def delete_car(self, idx: int):
        self.car_storage.pop(idx)
        print('Машина удалена')

    def change_car(self, idx: int):
        self.car_storage[idx].mark = self.set_mark()
        self.car_storage[idx].year = self.set_year()
        self.car_storage[idx].price = self.set_price()
        self.car_storage[idx].mileage = self.set_mileage()

    def get_high_mileage(self):
        for i in self.car_storage:
            if i.calc_high_mileage():
                print(i)

    def get_sorted_price(self):
        self.car_storage.sort()
        print('Машины с самой низкой ценой:')
        for i in self.car_storage[:5]:
            print(i)
        print('Машины с самой высокой ценой')
        for i in self.car_storage[-5:]:
            print(i)


car_market = Carmarket()


def create_car():
    while True:
        choose = input('Выберите производителя:\n'
                       '1 - BMW\n'
                       '2 - Audi\n'
                       '3 - Bentley\n'
                       'Другое - закончить создание списка')
        if choose == '1':
            car_market.create_bmw()
        elif choose == '2':
            car_market.create_audi()
        elif choose == '3':
            car_market.create_bentley()
        else:
            break
    main_menu()


def delete_car():
    try:
        del_num = int(input('Введите номер машины из списка'))
        if 0 <= del_num < len(car_market.car_storage):
            car_market.delete_car(del_num)
        else:
            print('Машины нет в списке')
    except:
        print('Это не число')
    main_menu()


def change_car():
    try:
        value = int(input('Введите номер машины из списка'))
        if 0 <= value < len(car_market.car_storage):
            car_market.change_car(value)
        else:
            print('Машины нет в списке')
    except:
        print('Это не число')
    main_menu()


def main_menu():
    while True:
        choose = input('Выберите пункт меню:\n'
                       '1 - создать список машин\n'
                       '2 - просмотр всех машин\n'
                       '3 - удаление машины\n'
                       '4 - изменить машину\n'
                       '5 - посмотреть машины с большым пробегом\n'
                       '6 - получить 5 машин с самой большой/маленькой ценой\n'
                       'Другое - завершение программы')
        if choose == '1':
            create_car()
        elif choose == '2':
            car_market.get_all_cars()
        elif choose == '3':
            delete_car()
        elif choose == '4':
            change_car()
        elif choose == '5':
            car_market.get_high_mileage()
        elif choose == '6':
            car_market.get_sorted_price()
        else:
            break


if __name__ == '__main__':
    main_menu()
