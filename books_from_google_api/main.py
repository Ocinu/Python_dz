from parse import get_sorted_books
from filter import Filter
from files import Files
from library import Library

files = Files()

# загрузка сохраненных книг чтобы была возможность дозаписи из нового поиска
storage_book = Library()
storage_book.load_storage()


def print_info(books_list):
    for i in books_list:
        print(i)


def main_menu():
    choose = input('Начать новый поиск - 1\n'
                   'Просмотр сохраненных книг - 2')
    if choose == '1':
        get_new_books()
    elif choose == '2':
        load_books()


def get_new_books():
    book_name = input('Введите название книги (может быть не полным):')
    new_books = get_sorted_books(str(book_name))
    print_info(new_books)
    book_filter(new_books)


# фильтрация поиска, добавление к уже загруженным и сохранение общего списка в файл
def book_filter(new_books):
    storage_book.load_storage()
    filtered_search = Filter(new_books)
    while True:
        choose = input('Выберите параметр фильтрации:\n'
                       '1 - по автору (не полное имя автора)\n'
                       '2 - по заголовку (не полный заголовок)\n'
                       '3 - по описанию (не полное описание)\n'
                       '4 - по цене (промежуток от и до)\n'
                       'Любой другой ввод - закончить фильтрацию и сохранить результат\n')
        if choose == '1':
            partial_name = input('Введите имя автора (не полное):')
            filtered_search.sort_author(str(partial_name))
            print_info(filtered_search.filtered_list)
        elif choose == '2':
            partial_title = input('Введите заголовок (не полный)')
            filtered_search.sort_title(str(partial_title))
            print_info(filtered_search.filtered_list)
        elif choose == '3':
            partial_disk = input('Введите описание (не полное)')
            filtered_search.sort_disc(str(partial_disk))
            print_info(filtered_search.filtered_list)
        elif choose == '4':
            partial_price = input('Введите цену (промежуток от и до через пробел')
            partial_price.split(' ')
            try:
                start_price = float(partial_price[0])
                end_price = float(partial_price[-1])
                filtered_search.sort_price(start_price, end_price)
            except:
                ValueError('Введите два числа через пробел')
            print_info(filtered_search.filtered_list)
        else:
            break
    storage_book.add_new(filtered_search.filtered_list)
    files.save_books(storage_book.library)
    main_menu()


def load_books():
    storage_book.load_storage()
    storage_book.get_library()
    while True:
        choose = input('1 - удалить книгу из списка\n'
                       '2 - отметь книгу как прочтенную\n'
                       'Любой другой ввод - сохранить список и выйти в меню\n')

        if choose == '1':
            try:
                del_num = int(input('Введите номер книги из списка'))
                if 0 <= del_num < len(storage_book.library):
                    storage_book.delete_book(del_num)
                else:
                    print('Книга не в списке')
            except:
                print('Это не число')
        elif choose == '2':
            try:
                mark_num = int(input('Введите номер книги из списка'))
                if 0 <= mark_num < len(storage_book.library):
                    storage_book.mark_read(mark_num)
                else:
                    print('Книга не в списке')
            except:
                print('Это не число')
        else:
            break
    files.save_books(storage_book.library)
    main_menu()


if __name__ == '__main__':
    main_menu()
