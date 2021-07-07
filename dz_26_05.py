"""
1. Создать класс описывающий источник данных в XML формате.
Добавить адаптер для класса Program работающего с JSON форматом данных.
"""
import csv
import json
import pandas as pd


class CSVData:
    def __init__(self):
        self.file_name = "data.csv"

    def save_csv(self, data):
        with open(self.file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            return True

    def load_csv(self):
        with open(self.file_name) as file:
            reader = csv.reader(file)
            return reader


class Program:
    def __init__(self):
        self.temp = Adapter()

    def load_data(self):
        self.temp.csv_to_json()
        return self.temp

    def save_data(self, data):
        self.temp.json_to_csv(data)
        return True


class Adapter:
    def __init__(self):
        self.csv_data = CSVData()

    def csv_to_json(self):
        temp = self.csv_data.load_csv()
        temp = pd.read_csv(temp)
        return temp

    def json_to_csv(self, data):
        data = pd.read_json(data)
        self.csv_data.save_csv(data)
        return True


test_json = json.dumps(
                            {
                                "Product": {"0": "Desktop Computer", "1": "Tablet", "2": "iPhone", "3": "Laptop"},
                                "Price": {"0": 700, "1": 250, "2": 800, "3": 1200}
                            }
                        )
print(type(test_json))

temp = json.loads(test_json)
print(type(temp))

for i in temp:
    print(type(i), i)


# p = Program()
# p.save_data(test_json)

"""
2. Создать декоратор для системы оповещений (слак, фейсбук, смс и тд). Не делать чистое наследование
"""

"""
3. Создать фасад для взаимодействия пользователя с системой заказа товаров по телефону.
"""
