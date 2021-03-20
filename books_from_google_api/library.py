from files import Files

file = Files()


class Library:
    def __init__(self):
        self.library = []

    def load_storage(self):
        self.library = file.load_books()
        return True

    def add_new(self, new_books: list):
        self.library.append(new_books)
        return True

    def get_library(self):
        for idx, i in enumerate(self.library):
            print(f'{idx} - {i}')
        return True

    def delete_book(self, idx: int):
        self.library.pop(idx)
        print('Книга удалена')
        return True

    def mark_read(self, idx: int):
        self.library[idx]['Read'] = True
        return True


