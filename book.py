class Book:
    def __init__(self, title, price, author, bsn, availabile):
        self.title = title
        self.price = price
        self.author = author
        self.bsn = bsn
        self.availabile = availabile
        
    def say_info(self):
        print(f"Book info: {self.title} by {self.author}, Price: {self.price}, BSN: {self.bsn}, Available: {self.availabile}")
        
    def borrow(self):
        if self.availabile == True:
            print(f"You have borrowed {self.title}.")
            self.availabile = False
            
        else:
            print(f"Sorry, {self.title} is not available for borrowing.")
        
    def return_book(self):
        if self.availabile == False:
            print(f"You have returned {self.title}.")
            self.availabile = True
            
        else:
            print(f"{self.title} was not borrowed.")



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

