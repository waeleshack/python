class Person:
    def __init__(self, f_name: str, l_name: str, salary: float):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.available = True


    def person_info(self):
        print(f"{self.f_name} {self.l_name}, Salary: {self.salary}")   
        print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+") 

    def check_in(self):
        self.available = True
        print(f"{self.f_name} {self.l_name} is now checked in.")
        print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+") 


    def check_out(self):
        self.available = False
        print(f"{self.f_name} {self.l_name} is now checked out.")
        print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+") 







