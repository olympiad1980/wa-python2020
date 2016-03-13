class Book:

    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return 'The Book {!r}, {!r}, {!r}'.format(self.title, self.year, self.genre)


    #def __str__(self):




# Задание: создайте несколько объектов класса Book
# и выведите их на экран

book = Book('99 Франков', 2000, 'роман')
print(book.title)
print(book.year)
print(book.genre)