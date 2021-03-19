"""
Задание: Написать класс "Группа студентов", нужно использовать класс "Студент" из прошлого задания.
В классе должны быть реализованы следующие возможности:
1) Создать студента
 - Функция должна принимать все поля необходимые для работы класса "Студент"
 - Функция должна возвращать True, если студент создан, иначе False если произошла ошибка
2) Изменить студента
 - Функция должна принимать все поля необходимые для работы класса "Студент" и почту студента которого необходимо получить
 - Функция должна возвращать True, если студент изменен, иначе False если произошла ошибка
3) Посмотреть студентов
 - Функция должна возращать список студентов.
4) Удалить студента
 - В функцию в качестве аргумента должен передаваться почта студента
 - Функция должна возвращать True, если пользователь удален, иначе False
5) Получить всех студентов у которых оценка >= n
 - В функцию в качестве аргумента должна передаваться переменная n
6) Получить студента по почте
 - В качестве аргумента функция принимает почту студента
 - Функция должна возвращать обьект студента, если он найден, иначе None
В качестве выполненного ДЗ отправить ссылку на репозиторий GitHub
"""
from dz_09_03 import Student


class StudentDatabase:

    def __init__(self):
        self.students = []

    # Создать студента
    def add_students(self, name, rating, email, password, confirm_password, attendance):
        try:
            student = Student(name, rating, email, password, confirm_password, attendance)
        except ValueError as e:
            print(e)
            return False
        self.students.append(student)
        return True

    # Проверка на наличие студента в базе
    def check_student_exist(self, mail):
        for idx, user in enumerate(self.students):
            if user.mail == mail:
                return idx
        return None

    # Изменить студента
    def edit_student(self, find_mail, name, rating, email, password, confirm_password, attendance):
        student_idx = self.check_student_exist(find_mail)
        if student_idx is None:
            print('Студент не найден')
            return False
        student = self.students[student_idx]
        student.name = name
        student.rating = rating
        student.email = email
        student.password = password
        student.confirm_password = confirm_password
        student.attendance = attendance
        return True

    # Посмотреть студентов (пароли остаются скрытыми)
    def get_students(self):
        return '\n'.join([f'{x.name}\n' \
                          f'{x.email}\n' \
                          f'{x.rating}\n' \
                          f'{x.attendance}\n'
                          for x in self.students])

    # Удалить студента
    def delete_student(self, mail):
        student_idx = self.check_student_exist(mail)
        if student_idx is None:
            print('Студент не найден')
            return False
        self.students.pop(student_idx)
        return True

    # Получить всех студентов у которых оценка >= n
    def get_students_rated(self, n):
        rated_list = []
        for x in self.students:
            if x.rating >= n:
                rated_list.append(f'{x.name}, {x.email}, {x.rating}')
        if len(rated_list) > 0:
            return rated_list
        else:
            print('Студенты не найдены')
            return None

    # Получить студента по почте
    def get_student_info(self, find_mail):
        student_idx = self.check_student_exist(find_mail)
        if student_idx is None:
            print('Студент не найден')
            return False
        student = self.students[student_idx]
        return f'{student.name}, ' \
               f'{student.email}, ' \
               f'{student.rating}, ' \
               f'{student.attendance}, ' \
               f'{student.password}, ' \
               f'{student.confirm_password}'
