"""
Задание:
1) Запросить у пользователя название книги (Оно может быть не полным) и найти по нему все книги которые есть в Google Books.
2) Добавить в программу возможность фильтровать результат по
  * Автору (Не полное имя автора)
  * Заголовку (Не полный заголовок)
  * Описанию (Не полное описание)
  * Цене (Промежуток от и до)
Пользователя может несколько раз фильтровать один результат поиска в Google Books.
3) Добавить в программу возможность сохранять понравившиеся книги в файл.
5) Удалять книги из файла
6) Помечать как прочитанные книги
7) Отображать книги из файла
Документация по API Google books https://developers.google.com/books/docs/v1/reference/volumes
Код: https://github.com/brusencov/oop/blob/master/book.py
В качестве выполненного ДЗ нужно отправить ссылку на гитхаб в котором будет находится решение задачи
"""

import requests
import json

base_url = 'https://www.googleapis.com/books/v1/volumes?q=%s'
FILE = 'books.json'


def save_info(books):
    with open(FILE, 'w') as f:
        f.write(json.dumps(books))
        f.close()


def load_info():
    with open(FILE, 'r') as f:
        return json.loads(f)


def print_info(books_list):
    for i in books_list:
        print(i)


def get_google_books(search):
    resp = requests.get(base_url % search)
    json_resp = json.loads(resp.content)
    if 200 <= resp.status_code <= 299:
        return json_resp
    raise Exception(json_resp['error']['message'])


def book_to_dict(book):
    base_book = {
        'author': '',
        'title': '',
        'description': '',
        'price': 0.0,
        'buy_link': None
    }
    if 'volumeInfo' in book:
        if 'title' in book['volumeInfo']:
            base_book['title'] = book['volumeInfo']['title']
        if 'description' in book['volumeInfo']:
            base_book['description'] = book['volumeInfo']['description']
        if 'authors' in book['volumeInfo']:
            base_book['author'] = book['volumeInfo']['authors']
    if 'saleInfo' in book:
        if 'buyLink' in book['saleInfo']:
            base_book['buy_link'] = book['saleInfo']['buyLink']
        if 'listPrice' in book['saleInfo'] and 'amount' in book['saleInfo']['listPrice']:
            base_book['price'] = book['saleInfo']['listPrice']['amount']
    return base_book


def book_filter(books):
    choose = input('Выберите параметр фильтрации:\n'
                   '1 - по автору (не полное имя автора)\n'
                   '2 - по заголовку (не полный заголовок)\n'
                   '3 - по описанию (не полное описание)\n'
                   '4 - по цене (промежуток от и до)\n'
                   'Eny else - exit')
    if choose == '1':
        sort_author(books)
    elif choose == '2':
        sort_title(books)
    elif choose == '3':
        sort_disc(books)
    elif choose == '4':
        sort_price(books)
    else:
        save_info(books)
        print('закончить фильтрацию и сохранить')


def sort_author(books):
    sorted_books = []
    partial_name = input('Введите имя автора (не полное):')
    for i in books:
        print(i['author'])
        if partial_name in str(i['author']):
            sorted_books.append(i)
    print_info(sorted_books)
    book_filter(sorted_books)


def sort_title(books):
    sorted_books = []
    partial_title = input('Введите заголовок (не полный)')
    for i in books:
        if partial_title in str(i['description']):
            sorted_books.append(i)
    print_info(sorted_books)
    book_filter(sorted_books)


def sort_disc(books):
    sorted_books = []
    partial_disk = input('Введите описание (не полное)')
    for i in books:
        if partial_disk in str(i['title']):
            sorted_books.append(i)
    print_info(sorted_books)
    book_filter(sorted_books)


def sort_price(books):
    pass


if __name__ == '__main__':
    book_name = input('Введите название книги (может быть не полным):')
    json_resp = get_google_books(book_name)
    books = [book_to_dict(x) for x in json_resp['items']]
    print_info(books)
    book_filter(books)
