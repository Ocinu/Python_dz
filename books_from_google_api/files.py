import json


class Files:
    def __init__(self):
        self.file = 'books.json'
        self.storage = None

    def save_books(self, books):
        with open(self.file, 'w') as f:
            f.write(json.dumps(books))
            print('Книги сохранены')

    def load_books(self):
        with open(self.file, 'r') as f:
            self.storage = json.load(f)
            return self.storage
