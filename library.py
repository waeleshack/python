
from book import Book
from Person import Person



class Library:
    def __init__(self, address: str, phone: str):
        self.address = address
        self.phone = phone
        self.books = []
        self.persons = []

    def say_info(self):
        print(f"Library Address: {self.address}, Phone: {self.phone}")

    def say_books(self):
        for book in self.books:
            book.say_info()
            print()

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
       


    def search_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.say_info()
                return book
        print("Book not found.")
       
        return None

    def say_persons(self):
        for person in self.persons:
            print(f"{person.f_name} {person.l_name}, Salary: {person.salary}")
          

    def add_person(self, person: Person):
        self.persons.append(person)
        print(f"Person '{person.f_name} {person.l_name}' added to the library.")
        









