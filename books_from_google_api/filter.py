

class Filter:
    def __init__(self, filtered_list):
        self.filtered_list = filtered_list

    def sort_author(self, partial_name: str):
        sorted_books = []
        for i in self.filtered_list:
            if partial_name in str(i['author']):
                sorted_books.append(i)
        self.filtered_list = sorted_books
        return self.filtered_list

    def sort_title(self, partial_title: str):
        sorted_books = []
        for i in self.filtered_list:
            if partial_title in str(i['description']):
                sorted_books.append(i)
        self.filtered_list = sorted_books
        return self.filtered_list

    def sort_disc(self, partial_disk: str):
        sorted_books = []
        for i in self.filtered_list:
            if partial_disk in str(i['title']):
                sorted_books.append(i)
        self.filtered_list = sorted_books
        return self.filtered_list

    def sort_price(self, start_price: float, end_price: float):
        sorted_books = []
        for i in self.filtered_list:
            if start_price < float(i['price']) < end_price:
                sorted_books.append(i)
        self.filtered_list = sorted_books
        return self.filtered_list
