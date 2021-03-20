"""
Задание: Написать класс студент.
В студенте должны быть следующие поля:
1) Фио
 - Проверить, что в ФИО содержится более 3-х слов
 - Проверить, что ФИО - строка
2) Оценка
 - Проверить, что оценка - число
 - Проверить, что оценка находится в диапазоне от 1 до 12 (Включительно)
3) Почта
 - Проверить, что почта - строка
 - Сделать валидацию для почты (Можно использовать regex или метод find в Python)
4) Пароль
 - Проверить, что пароль - строка
 - Длина пароля >= 8
 - Есть спец. символ в пароле
 - Есть большая и маленькая буква
 - Есть число
5) Подтверждение пароля
 - Проверить, что значение - строка
 - Подтверждение пароля должно совпадать с паролем
6) Посещаемость пар
 - Проверить, что значение - число
 - Посещаемость должна задаваться в процентах, в диапазоне от 0 до 100%
Все поля в классе должны быть реализованы через property
В качестве выполненного ДЗ отправить ссылку на репозиторий на GitHub
"""
import re


class Student:

    def __init__(self, name, rating, email, password, confirm_password, attendance):
        self.name = name
        self.rating = rating
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.attendance = attendance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if len(value.split(' ')) < 4 and value.split(' ')[-1] != '' and value.split(' ')[0] != '':
                self._name = value.title()
            else:
                raise ValueError('В имени неможет быть больше 3-х слов')
        else:
            raise ValueError('Имя должно быть строкой')

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if isinstance(value, int) and 1 <= value <= 12:
            self._rating = value
        else:
            raise ValueError('Оценка должна быть от 1 до 12 и тип данных int')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.search(r'(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})', str(value)):
            self._email = value
        else:
            raise ValueError('Введите корректный электронный адресс')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if re.search(r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15})', str(value)):
            self._password = value
        else:
            raise ValueError('Пароль должен содержать от 8 до 15 символов'
                             'должна быть минимум одна заглавная буква'
                             'должна быть минимум одна прописная буква'
                             'должна быть минимум одна цыфра')

    @property
    def confirm_password(self):
        return self._confirm_password

    @confirm_password.setter
    def confirm_password(self, value):
        if isinstance(value, str) and value == self.password:
            self._confirm_password = value
        else:
            raise ValueError('Валидация пароля не пройдена!')

    def check_password(self, confirm_password):
        if self.password == confirm_password:
            return True
        else:
            return False

    @property
    def attendance(self):
        return self._attendance

    @attendance.setter
    def attendance(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._attendance = value
        else:
            raise ValueError('Должно быть число от 0 до 100')
