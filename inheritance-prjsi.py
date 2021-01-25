#parent class
class Website:
        "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def loginInfo(self):
        print(self.name + " " + self.surname)

#child class        
class Website1(Website):
    "child"
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids
       
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)

#child class        
class Website2(Website):
    "child"
    def __init__(self, name, surname, email):
        Website.__init__(self, name, surname)
        self.email = email
       
    def login(self):
        print(self.name + " " + self.surname + " " + self.email)
        
        
p1 = Website("name", "surname") 
p2 = Website1("name","surname",123)
p3 = Website2("name","surname", "adasd@adad.com")        
        