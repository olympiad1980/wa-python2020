class Book:

    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def __repr__(self):
        return 'The Book {!r}, {!r}, {!r}'.format(self.title, self.year, self.genre)


    def __str__(self):
        return 'Book is'




book = Book('99 Francs', 2000, 'novel')
print(book.title)
print(book.year)
print(book.genre)
print (book)