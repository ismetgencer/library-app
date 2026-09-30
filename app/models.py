class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

books = [
    Book("1984", "George Orwell", "123"),
    Book("Dune", "Frank Herbert", "456"),
    Book("Sefiller", "Victor Hugo", "789"),
    Book("Suç ve Ceza", "Fyodor Dostoyevski", "101"),
    Book("Simyacı", "Paulo Coelho", "102"),
    Book("Kürk Mantolu Madonna", "Sabahattin Ali", "103"),
    Book("Tutunamayanlar", "Oğuz Atay", "104"),
    Book("Yüzyıllık Yalnızlık", "Gabriel García Márquez", "105"),
    Book("Hayvan Çiftliği", "George Orwell", "106"),
    Book("Satranç", "Stefan Zweig", "107"),
    Book("İnce Memed", "Yaşar Kemal", "108"),
    Book("Fahrenheit 451", "Ray Bradbury", "109"),
]

members = [
    Member("Ali", 1),
    Member("Ayşe", 2),
    Member("Mehmet", 3),
    Member("Zeynep", 4),
    Member("Can", 5),
    Member("Elif", 6),
    Member("Burak", 7),
]

members[0].borrow(books[0])
members[0].borrow(books[9])
members[1].borrow(books[1])
members[2].borrow(books[3])
members[3].borrow(books[2])
members[5].borrow(books[5])

def find_book(title):
    for book in books:
        if book.title == title:
            return book
    return None

def find_member(member_id):
    for member in members:
        if member.member_id == member_id:
            return member
    return None

def next_member_id():
    if not members:
        return 1
    return max(member.member_id for member in members) + 1
