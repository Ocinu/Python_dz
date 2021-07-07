"""
Задание #4:
Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
Реализуйте функцию для получения книг по всем параметрам класса.
"""


class Book:
    def __init__(self, name, date, prod, genre, autor, price):
        self.name = name
        self.date = date
        self.prod = prod
        self.genre = genre
        self.autor = autor
        self.price = price

    def __str__(self):
        return [self.name, self.date, self.prod, self.autor, self.price]

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
    def date(self, value):
        self._date = value

    @property
    def prod(self):
        return self._prod

    @prod.setter
    def prod(self, value):
        self._prod = value

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def get_name(self):
        print(f'{self.name}, {self.date}, {self.autor}')

    def get_prod(self):
        print(f'{self.prod}, {self.genre}')


"""
Задание #5:
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
    - Проверка на равенство радиусов двух окружностей
    (операция = =);
    - Сравнения длин двух окружностей (операции >, <,
    <=,>=);
    - Пропорциональное изменение размеров окружности,
    путем изменения ее радиуса (операции + - += -=).
"""


class Circle:
    def __init__(self, radius):
        self.circle_len = 3.14 * self.radius ^ 2
        self.radius = radius

    # Проверка на равенство
    def __eq__(self, other):
        return self.radius == other.radius

    # Сравнения длин
    def __lt__(self, other):
        return self.circle_len < other.circle_len

    def __gt__(self, other):
        return self.circle_len > other.circle_len

    def __ge__(self, other):
        return self.circle_len >= other.circle_len

    def __le__(self, other):
        return self.circle_len <= other.circle_len

    # тут я могу ошибатся, использую информацию которую нашел в интернете.
    # Полагаю, что после увеличения радиуса circle_len будет переопределен в __init__
    def __pos__(self):
        return Circle(+self.radius)

    def __neg__(self):
        return Circle(-self.radius)


"""
Задание #6:
Создайте базовый класс Shape для рисования плоских
фигур.
Определите методы:
    - Show() — вывод на экран информации о фигуре;
    - Save() — сохранение фигуры в файл;
    - Load() — считывание фигуры из файла.
Определите производные классы:
    - Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
    - Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
    - Circle — окружность с заданными координатами центра и радиусом
"""


class Shape:
    def __init__(self):
        self.figure = None
        self.file_name = None

    def show(self):
        print(self.figure)

    def save(self):
        with open(self.file_name, 'w') as f:
            f.write(self.figure)

    def load(self):
        with open(self.file_name, 'r') as f:
            self.figure = f.read()


class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.figure = a * a
        self.file_name = 'square.txt'


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b
        self.figure = a * b
        self.file_name = 'rectangle.txt'


class Circle2(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r
        self.figure = 3.14 * r ^ 2
        self.file_name = 'circle.txt'
