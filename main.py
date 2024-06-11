from tkinter import *
from Book import Book


def books_page():
    # список для хранения книг
    list_books = []
    # создаем объект "книга"
    book = Book('Горе от ума', 'Грибоедов', '1822', 'В библиотеке')
    # добавить объект в список
    list_books.append(book)
    # сохранить созданный и заполненный список в переменную типа Variable
    list_books_var = Variable(value=list_books)
    # создать ListBox, шириной 100 символов, в котором будет отображаться список list_books
    books_list_view = Listbox(width=100, listvariable=list_books_var)
    # добавить ListBox в окно
    books_list_view.pack()
    # создаем метку
    book_title = Label(text='Название книги')
    # размещаем метку в окне
    book_title.pack()
    # создаем поле ввода
    book_title_entry = Entry()
    # размещаем поле ввода в окне
    book_title_entry.pack()
    # создаем метку
    book_author = Label(text='Автор книги')
    # размещаем метку в окне
    book_author.pack()
    # создаем поле ввода
    book_author_entry = Entry()
    # размещаем поле ввода в окне
    book_author_entry.pack()
    # создаем метку
    book_year = Label(text='Год выпуска книги')
    # размещаем метку в окне
    book_year.pack()
    # создаем поле ввода
    book_year_entry = Entry()
    # размещаем поле ввода в окне
    book_year_entry.pack()
    # создаем метку
    book_status = Label(text='Статус книги')
    # размещаем метку в окне
    book_status.pack()
    # создаем поле ввода
    book_status_entry = Entry()
    # размещаем поле ввода в окне
    book_status_entry.pack()

    # кнопка для добавления книги
    add_button = Button(text='Добавить книгу', command=lambda: add_book())
    # размещаем кнопку в окне
    add_button.pack()

    # кнопка для бронирования книги
    reserve_button = Button(text='Забронировать книгу', command=lambda: reserve_book())
    # размещаем кнопку в окне
    reserve_button.pack()

    # кнопка для выдачи книги
    give_button = Button(text='Выдать книгу', command=lambda: give_book())
    # размещаем кнопку в окне
    give_button.pack()

    # кнопка для перемещения книги в библиотеку
    library_button = Button(text='В библиотеку', command=lambda: library_book())
    # размещаем кнопку в окне
    library_button.pack()
    # функция для добавления книги
    def add_book():
        # для считывания данных из поля ввода используется метод get()
        title = book_title_entry.get()
        author = book_author_entry.get()
        year = book_year_entry.get()
        status = book_status_entry.get()
        # создается объект
        new_book = Book(title, author, year, status)
        # добавить объект в список
        list_books.append(new_book)
        # обновить ListBox
        list_books_var.set(list_books)

    def reserve_book():
        # получить индекс выбранного элемента
        chosen_book = books_list_view.curselection()
        # изменяем статус выбранной книги
        list_books[chosen_book[0]].status = 'Забронирована'
        # обновляем ListBox
        list_books_var.set(list_books)


    def give_book():
        # получить индекс выбранного элемента
        chosen_book = books_list_view.curselection()
        # изменяем статус выбранной книги
        list_books[chosen_book[0]].status = 'На руках'
        # обновляем ListBox
        list_books_var.set(list_books)

    def library_book():
        # получить индекс выбранного элемента
        chosen_book = books_list_view.curselection()
        # изменяем статус выбранной книги
        list_books[chosen_book[0]].status = 'В библиотеке'
        # обновляем ListBox
        list_books_var.set(list_books)


class Main:
    # конструктор
    def __init__(self, root):
        # окно
        self.root = root
        # заголовок окна
        self.root.title('Книги')
        # размеры окна
        self.root.geometry('1000x500')

    # страница логина
    def login_page(self):
        # создаем метку
        user_name = Label(text='Ваше имя')
        # размещаем метку в окне
        user_name.pack()
        # создаем поле ввода
        user_name_entry = Entry()
        # размещаем поле ввода в окне
        user_name_entry.pack()

        # создаем метку
        user_last_name = Label(text='Ваша фамилия')
        # размещаем метку в окне
        user_last_name.pack()
        # создаем поле ввода
        user_last_name_entry = Entry()
        # размещаем поле ввода в окне
        user_last_name_entry.pack()

        # создаем метку
        user_surname = Label(text='Ваше отчество')
        # размещаем метку в окне
        user_surname.pack()
        # создаем поле ввода
        user_surname_entry = Entry()
        # размещаем поле ввода в окне
        user_surname_entry.pack()

        # создаем метку
        user_phone = Label(text='Ваш номер телефона')
        # размещаем метку в окне
        user_phone.pack()
        # создаем поле ввода
        user_phone_entry = Entry()
        # размещаем поле ввода в окне
        user_phone_entry.pack()

        # кнопка для отображения страницы книг
        submit_btn = Button(text='Войти', command=lambda: books_page())
        # размещаем кнопку в окне
        submit_btn.pack()


if __name__ == '__main__':
    root = Tk() # создаем корневой объект - окно
    main = Main(root) # создаем класс Main и передаем в него созданное окно
    main.login_page() # рисуем окно регистрации
    root.mainloop()
