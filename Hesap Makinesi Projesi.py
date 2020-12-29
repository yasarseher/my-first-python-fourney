#Calculator

# class -> init -> method/attribute -> funct vs method

class Calc(object):
    "calculator"
    #init metodu
    def __init__(self, a, b):
        "initialize values"
        #attribute
        self.value1 = a
        self.value2 = b
        
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
        
    def multiply(self):
        "multipication a*b = result -> return result"
        return self.value1 * self.value2
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
# ########################################
# #değerleri kodlama sırasında girilen hesap makinesi
# v1 = 5
# v2 = 3

# c1 = Calc(v1,v2)
# add_result = c1.add()
# multiply_result = c1.multiply()

# print("Add: {}, Multiply: {}".format(add_result,multiply_result))


# ########################################
# #değerleri input olarak konsola girilen hesap makinesi


while 1==1:  
    print("Choose add(+), multiply(*), division(/)")
    selection = input("select + or * or /: ")
    if selection == "+" or selection =="*" or selection =="/":
        v1 = int(input("first value: "))
        v2 = int(input("second value: "))

        c1 = Calc(v1,v2)

        if selection == "+":
            add_result = c1.add()
            print("Add: {},".format(add_result))

        elif selection == "*":    
            multiply_result = c1.multiply()
            print("Multiply: {}".format(multiply_result))
        
        elif selection == "/":    
            if v2 == 0:
                print("ZeroDivisionError")
            else:   
                division_result = c1.division()
                print("Division: {}".format(division_result))
                    
    else: 
        print("hatali giris yaptiniz!")























