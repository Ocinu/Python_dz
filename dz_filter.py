"""
Задание 1:
Дан словарь студентов с их оценками по каждому из предметов:
{'user1': {'math': 5, 'english': 12, 'geography': 7}, 'user2': {'math': 9, 'english': 3, 'geography': 11}, 'user3': {'math': 5, 'english': 8, 'geography': 6}, 'user4': {'math': 12, 'english': 10, 'geography': 10}, 'user5': {'math': 8, 'english': 5, 'geography': 5}, 'user6': {'math': 3, 'english': 7, 'geography': 1}, 'user7': {'math': 10, 'english': 9, 'geography': 9}, 'user8': {'math': 4, 'english': 2, 'geography': 1}, 'user9': {'math': 5, 'english': 2, 'geography': 6}, 'user10': {'math': 7, 'english': 9, 'geography': 9}, 'user11': {'math': 8, 'english': 12, 'geography': 12}, 'user12': {'math': 1, 'english': 6, 'geography': 5}, 'user13': {'math': 6, 'english': 12, 'geography': 11}, 'user14': {'math': 12, 'english': 5, 'geography': 6}, 'user15': {'math': 2, 'english': 1, 'geography': 6}}

Необходимо показать всех пользователей у которых оценка по математике
больше или равна 10, оценка по английскому выше средней по всем студентам,
и оценка по географии не меньше 7.
"""
import datetime

students = {'user1': {'math': 5, 'english': 12, 'geography': 7}, 'user2': {'math': 9, 'english': 3, 'geography': 11},
            'user3': {'math': 5, 'english': 8, 'geography': 6}, 'user4': {'math': 12, 'english': 10, 'geography': 10},
            'user5': {'math': 8, 'english': 5, 'geography': 5}, 'user6': {'math': 3, 'english': 7, 'geography': 1},
            'user7': {'math': 10, 'english': 9, 'geography': 9}, 'user8': {'math': 4, 'english': 2, 'geography': 1},
            'user9': {'math': 5, 'english': 2, 'geography': 6}, 'user10': {'math': 7, 'english': 9, 'geography': 9},
            'user11': {'math': 8, 'english': 12, 'geography': 12}, 'user12': {'math': 1, 'english': 6, 'geography': 5},
            'user13': {'math': 6, 'english': 12, 'geography': 11}, 'user14': {'math': 12, 'english': 5, 'geography': 6},
            'user15': {'math': 2, 'english': 1, 'geography': 6}}


def get_avg_eng(_dict) -> int:
    temp = 0
    for i in _dict.values():
        temp += i['english']
    return round(temp / len(_dict))


math_apprisal = dict(filter(lambda x: x[1]['math'] >= 10, students.items()))
eng_apprisal = dict(filter(lambda x: x[1]['english'] > get_avg_eng(students), students.items()))
geo_apprisal = dict(filter(lambda x: x[1]['geography'] < 7, students.items()))

print(list(math_apprisal.keys()))
print(list(eng_apprisal.keys()))
print(list(geo_apprisal.keys()))

"""
Задание 2:
Дана последовательность дат рождения пользователей записанная в строках:
['21/4/1977', '24/3/1980', '26/3/1963', '24/11/1952', '7/3/1991', '16/2/1974', '9/1/2002', '6/10/1964', '1/10/1999', '27/12/1989', '23/2/1958', '4/4/1991', '13/10/1970', '29/6/1992', '10/2/1974', '23/11/1987', '28/11/1973', '30/3/2001', '20/9/1961', '21/10/2000', '22/2/1956', '22/12/1973', '5/9/1983', '4/5/1962', '11/7/1982', '22/11/1958', '20/8/1954', '30/6/2010', '1/11/1982', '27/9/1991']
Необходимо отобразить всех пользователей, которые родились в промежуток дат
указанный пользователем. Начало и конец промежутка вводятся в формате
"день/месяц/год".
"""
users = ['21/4/1977', '24/3/1980', '26/3/1963', '24/11/1952', '7/3/1991', '16/2/1974', '9/1/2002', '6/10/1964',
         '1/10/1999', '27/12/1989', '23/2/1958', '4/4/1991', '13/10/1970', '29/6/1992', '10/2/1974', '23/11/1987',
         '28/11/1973', '30/3/2001', '20/9/1961', '21/10/2000', '22/2/1956', '22/12/1973', '5/9/1983', '4/5/1962',
         '11/7/1982', '22/11/1958', '20/8/1954', '30/6/2010', '1/11/1982', '27/9/1991']


def get_datetime_obj(date):
    list_value = date.split('/')
    day = int(list_value[0])
    month = int(list_value[1])
    year = int(list_value[2])
    return datetime.date(year, month, day)


first_date = input('First date')
second_date = input('Second date')

sorted_users = filter(lambda x: get_datetime_obj(first_date) < get_datetime_obj(x) < get_datetime_obj(second_date),
                      users)
print(list(sorted_users))
