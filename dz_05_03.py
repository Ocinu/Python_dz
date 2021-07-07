"""
Задание #1: Создайте структуру с именем student, содержащую поля: фамилия и инициалы, номер группы, успеваемость
(массив из пяти элементов). Создать массив из десяти элементов такого типа,
упорядочить записи по возрастанию среднего балла.
Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
"""


class Student:
    def __init__(self, name, group_num, perfomance):
        self.name = name
        self.group_num = group_num
        self.perfomance = perfomance

    def get_info(self):
        print(f'{self.name}; group: {self.group_num}; academic performance: {self.perfomance}')


student1 = Student('Ivanon I.I', 1, 4)
student2 = Student('Petrov A.I', 1, 5)
student3 = Student('Sidorov I.F', 2, 4)
student4 = Student('Popov S.I', 1, 3)
student5 = Student('Kruglov M.I', 2, 4)
students_list = [student1, student2, student3, student4, student5]
for i in students_list:
    if i.perfomance > 3:
        i.get_info()

"""
Задание #2: Создайте структуру с именем train, содержащую поля: 
название пункта назначения, номер поезда, время отправления. 
Ввести данные в массив из пяти элементов типа train, упорядочить элементы по номерам поездов. 
Добавить возможность вывода информации о поезде, номер которого введен пользователем. 
Добавить возможность сортировки массив по пункту назначения, 
причем поезда с одинаковыми пунктами назначения должны быть упорядочены по времени отправления.
"""


class Train:
    def __init__(self, dest, num, dep):
        self.destination = dest
        self.number = num
        self.departure = dep

    def get_info(self):
        print(f'{self.destination} {self.departure}')


train1 = Train('Lviv', 253, 18.40)
train2 = Train('Kyiv', 19, 12.30)
train3 = Train('Odesa', 456, 09.40)
train4 = Train('Rivne', 753, 20.10)
train5 = Train('Lytsk', 45, 06.35)
train_list = [train1, train2, train3, train4, train5]

train_num_list = []
destination_list = []
for i in train_list:
    train_num_list.append(i.number)

print(sorted(train_num_list))

choice = int(input('Enter train number'))
for i in train_list:
    if choice == i.number:
        i.get_info()

for i in train_list:
    destination_list.append(i.destination)

sort_list = sorted(train_list, key=lambda x: (x.destination[0], x.departure[0]))


"""
Задание #3:
Создайте класс Грузовик
У которого есть параметры Марка, год производства, максимальная скорость и кол-во км сколько ему нужно проехать
Класс должен уметь:
 - получать марку, год производства грузовика
 - получать за какое время грузовик проедет заданное количество км
"""


class Truck:
    def __init__(self, brand, prod_year, speed):
        self.brand = brand
        self.prod_year = prod_year
        self.speed = speed
        self.max_distance = 0

    def get_info(self):
        print(f'{self.brand}; {self.prod_year}; {self.max_distance}')

    def set_max_distance(self, max_distance):
        self.max_distance = max_distance

    def get_travel_time(self, distance):
        print(f'{distance / self.speed}')


volvo = Truck(brand='Volvo', prod_year=2000, speed=120)
volvo.set_max_distance(1200)
volvo.get_info()
volvo.get_travel_time(500)
