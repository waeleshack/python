
from book import Book
from Person import Person

person1 = Person("John", "Travolta", 5000)
person2 = Person("Will", "Smith", 6000)
person3 = Person("Arnold", "Schwarzenegger", 7000)
person4 = Person("Tom", "Hanks", 8000)
person5 = Person("Brad", "Pitt", 9000)
person6 = Person("Sylvester", "Stallone", 10000)
person7 = Person("Angelina", "Jolie", 11000)
person8 = Person("Morgan", "Freeman", 12000)
person9 = Person("Scarlett", "Johansson", 13000)
person10 = Person("Robert", "Downey", 14000)

person1.check_in()
person2.check_in()
person3.check_in()
person4.check_in()
person5.check_in()
person6.check_in()
person7.check_in()
person8.check_in()
person9.check_in()
person10.check_in()
person1.check_out()

person1.person_info()



Book1 = Book("Harry Potter", 20, "JK Rowling", 1234, True)
Book2 = Book("The Lord of the Rings", 30, "JRR Tolkien", 5678, True)
Book3 = Book("The Hobbit", 25, "JRR Tolkien", 9012, True)
Book4 = Book("The Catcher in the Rye", 15, "JD Salinger", 3456, True)
Book5 = Book("To Kill a Mockingbird", 20, "Harper Lee", 7890, True)
Book6 = Book("1984", 25, "George Orwell", 1234, True)
Book7 = Book("Brave New World", 30, "Aldous Huxley", 5678, True)
Book8 = Book("The Great Gatsby", 20, "F. Scott Fitzgerald", 9012, True)
Book9 = Book("The Lord of the Rings", 30, "JRR Tolkien", 5678, True)
Book10 = Book("The Hobbit", 25, "JRR Tolkien", 9012, True)  
Book11 = Book("The Catcher in the Rye", 15, "JD Salinger", 3456, True)  
Book12 = Book("To Kill a Mockingbird", 20, "Harper Lee", 7890, True)


Book.borrow(Book1)
Book.return_book(Book2)
Book.borrow(Book3)
Book.return_book(Book4)
Book.borrow(Book5)
Book.return_book(Book6)
Book.borrow(Book7)
Book.return_book(Book8)
Book.borrow(Book9)
Book.return_book(Book10)
Book.borrow(Book11)
Book.return_book(Book12)
