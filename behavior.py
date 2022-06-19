class Student:
    school="akirachix"
    def __init__(self,country,age,name):
        self.name=name
        self.age=age
        self.country=country
        
    def full_name(self,first_name,given_name):
        self.first_name=first_name
        self.given_name=given_name
        return f" My  full name is {self.first_name + self.given_name}"
    
    def year_of_birth(self):
      return f"your year of birth is {2022-self.age}"
    
    def initials(self):
        return f"My initials are {self.first_name[0] + self.given_name[0]}"
        
    
   
   