class Person:
    def __init__(self, f_name: str, l_name: str, salary: float):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.available = True


    def person_info(self):
        print(f"{self.f_name} {self.l_name}, Salary: {self.salary}")    

    def check_in(self):
        self.available = True
        print(f"{self.f_name} {self.l_name} is now checked in.")

    def check_out(self):
        self.available = False
        print(f"{self.f_name} {self.l_name} is now checked out.")


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