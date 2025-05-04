class Book:
    def __init__(self, title, price, author, bsn, availabile):
        self.title = title
        self.price = price
        self.author = author
        self.bsn = bsn
        self.availabile = availabile
        
    def say_info(self):
        print(f"Book info: {self.title} by {self.author}, Price: {self.price}, BSN: {self.bsn}, Available: {self.availabile}")
        print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")

        
    def borrow(self):
        if self.availabile == True:
            print(f"You have borrowed {self.title}.")
            self.availabile = False
            print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")

            
        else:
            print(f"Sorry, {self.title} is not available for borrowing.")
            print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")

        
    def return_book(self):
        if self.availabile == False:
            print(f"You have returned {self.title}.")
            self.availabile = True
            print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
            
        else:
            print(f"{self.title} was not borrowed.")
            print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")










