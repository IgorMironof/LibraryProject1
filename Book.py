class Book:
    # конструктор
    def __init__(self, title, author, year, status):
        # название
        self.title = title
        # автор
        self.author = author
        # год издания
        self.year = year
        # статус книги
        self.status = status

    # фукнкция для вывода книги в список
    def __str__(self):
        # возврат строчки с названием, автором, годом выпуска и статусом
        return self.title + ' ' + self.author + ' ' + self.year + ' ' + self.status