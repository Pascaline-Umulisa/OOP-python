class Student:
    school="AkiraChix"
    def __init__(self,first_name, last_name, age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country 
    def greeting(self):
        return f"Hello {self.name} from {self.country}, welcome to {self.school}"
    def full_name(self):
        return f" My name is {self.first_name} {self.last_name}"
    def year_of_birth(self):
        return f"you were born in {2022-self.age} " 
    def initials(self):
        return f"{self.first_name[0]}{self.last_name[0]} "
    