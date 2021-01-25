#parent class
class Animal:
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
    
    def walk(self):
        print("animal walk")
        

#child class
class Monkey(Animal):
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("monkey is created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")

#child class        
class Bird(Animal):
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("bird is created")
        
    def toString(self):
        print("bird")
        
    def fly(self):
        print("bird can fly")

m1 = Monkey()
b1 = Bird()
b1.fly()
m1.climb()
m1.walk()
print("---------")
b1.walk()
m1.toString()
b1.toString()