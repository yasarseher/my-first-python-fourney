from abc import ABC, abstractmethod

class Animal(ABC): # super class
   
    @abstractmethod
    def walk(self): pass
    
    @abstractmethod
    def run(self): pass
      

class Bird(Animal): # sub class
    def __init__(self):
        print("bird")
    
    def walk(self):
        print("walk") 
    
    def run(self): 
        print("run")
        
b1 = Bird()  
b1.run()

# parent/super class larda kullanılan methodları 
# clild/sub class larda da yeniden kullanmak zorundayız
# abstract classlar ve methodların normal class ve methoddan farkı bu.