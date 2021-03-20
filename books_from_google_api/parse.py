import json

import requests

base_url = 'https://www.googleapis.com/books/v1/volumes?q=%s'


def get_google_books(book_name):
    resp = requests.get(base_url % book_name)
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


def get_sorted_books(book_name):
    json_resp = get_google_books(book_name)
    new_books_list = [book_to_dict(x) for x in json_resp['items']]
    return new_books_list
