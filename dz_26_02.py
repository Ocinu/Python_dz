"""
Задание:
1) В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют
средний балл за национальной шкалой более «4».
"""
import json

FILE = 'list.json'


def source_file():
    appraisals = {'Ivanov': 5,
                  'Petrov': 4,
                  'Sidorov': 2}

    with open(FILE, 'w') as f:
        f.write(json.dumps(appraisals))


def main_prog():
    with open(FILE, 'r') as f:
        apr = json.load(f)

    for i in apr.keys():
        if apr[i] > 4:
            print(i.upper())


"""
2) Из текстового файла удалить все слова, содержащие от трех до пяти символов, но при этом из каждой строки 
должно быть удалено только четное количество таких слов.
"""
FILE2 = 'text.txt'

with open(FILE2, 'r') as f:
    text = f.read()

text = text.split('\n')

for i in text:
    n = i.split(' ')
    count = 0
    for j in n:
        if count % 2 == 0:
            if 2 < len(j) < 5:
                i = i.replace(j, '')
        count += 1

    print(i)
"""
3) Из текста программы выбрать все числа (целые и вещественные) и записать их в файл g в виде: 
число 1 – номер строки, число 2 – номер строки и так далее.
В качестве выполненного ДЗ отправить ссылку на проект GitHub в котором будет находится код.
"""
new = []
count = 0
for i in text:
    count += 1
    i = i.split(' ')
    for j in i:
        if j.isdigit():
            new.append(f'{j} - {count}')

with open('g.txt', 'w') as f:
    f.write(str(new))
