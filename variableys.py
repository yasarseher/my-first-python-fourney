# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:16:54 2020

@author: Yasar
"""
#%% variables
#variable (değişken)

#variable
#function
#object

var1 = 10 #integer
var2 = 15 #integer

gun="pazartesi" #string

var3 = 10.0

print(type(var3))

#%% strings
#string

s="bugun gunlerden pazartesi"

variable_type = type(s)
print(type(s))

var1 = "ankara"
var2 = "istanbul"
var3 = var1+var2
print(var3)
len(var3)
print(var3[6])

#%% numbers
#numbers

integer_deneme = -50
float_deneme = -22.5

#%% built in function

str1="deneme"
float1=10.6
float(10.2)
int(float1)
round(float1)


#%% user defined function

var1=20
var2=50

#output=var1*var2-var2


#fonksiyon parametresi = input
def benim_ilk_func(var1,var2):
    """
    bu benim ilk denemem
    parametre:
    
    return:

    """
    output=var1*var2-var2
    return output

sonuc=benim_ilk_func(var1,var2)
print(sonuc)



def deneme1():
    print("bu benim ikinci denemem")



#%% default ve flexible functions

#default f: cemberin cevre uzunlugu

def cember_cevre_hesapla(r,pi=3.14):
    
    """
    cemberin cevresini hesapla
    input(parametre): r,pi
    output=cemberin cevresi
    return:
        
    """
    output = 2*pi*r
    return output

#flexible f

def hesapla(boy,kilo,*args):
    print(len(args))
    output=(boy+kilo)*args[4]
    return output



# def hesapla(boy,kilo,yas):
#     output=(boy+kilo)*yas
#     return output


#%% QUIZ

#int variable yas
#string name isim
#fonksiyonu olacak
#fonksiyon print(type(),len,float())
#*args soyisim
#default parametre ayakkabı numarası

yas=10
name="ali"
soyisim="veli"

def function_quiz(yas,name,*args,ayakkabi_numarasi=35):
    print("Cucugun İsmi: ", name, "Yasi: ", yas,"Ayakkabi Numarasi: ",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output=args[0]*yas
    return output

sonuc = function_quiz(yas,name,soyisim)
print("args[0]*yas",sonuc)

#%% Lambda function

def hesapla(x):
    output=x*x
    return output

sonuc=hesapla(3)


def hesapla(x):
    return x*x

sonuc=hesapla(3)


sonuc2=lambda x:x*x**x
print(sonuc2(3))















