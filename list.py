# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 22:40:18 2020

@author: Yaşar
"""

#%% list

liste = [1,2,3,4,5,6]
print(type(liste))

liste2 = ["pazartesi","salı","carsamba"]
print(type(liste2))


value = liste[1]
print(value)

last_value = liste[-1]
print(last_value)

liste_divide = liste[0:3]

liste.append(7)

liste.remove(7)

liste.reverse()

string_int_liste = [1,2,3,"aa","bb"]

#%% tuple

t = (1,2,3,3,4,5,6)

t[2]
t.count(3)
t.index(2)

#%% dictionary

dictionary = {"ali":32,"veli":45,"ayse":13}

dictionary["ali"]
type(dictionary["ali"])

#ali,veli,ayse =keys
#32,45,13 = values

def deneme():
    dictionary = {"ali":32,"veli":45,"ayse":13}
    return dictionary

dic = deneme()
type(dic)


#%% conditionals
#if else statement

var1 = 20
var2 = 20

if (var1 > var2):
    print("var1 büyüktür var2")
    
elif (var1 == var2):
    print("var1 eşittir var2")
    
else:
    print("var2 büyüktür var1")


liste = [1,2,3,4,5]

if 6 in liste:
    print("evet 6 değeri listenin içinde")
else:
    print("hayır listede 6 değeri yok")
    
    
    
    
  liste = [1,2,3,4,5]

value = 3
if value in liste:
    print("evet {} degeri listenin icinde".format(value))
else:
    print("hayır listede {} değeri yok".format(value))
    
      
dictionary.keys()
Out[78]: dict_keys(['ali', 'veli', 'ayse'])

dictionary.values()
Out[79]: dict_values([32, 45, 13])
    


keys = dictionary.keys()

if "osman" in keys:
    print("evet") 
else:
    print("hayir")
    
    
#%%

#1630. yil == 17. yuzyil
#109. yil == 2. yuzyil
#2000.yil == 20. yuzyil

#metod yazin. 
    #input integer yillar
    #output yuzyil
    
# KISIT: Milattan oncesi yok + 2005 den sonrasi yok
# input = year >> 1 <= year <= 2005


#%% BENIM YUZYIL KODU

def year2Century(year):
    
    
    yuzyil = year/100

    if (int(yuzyil) < yuzyil):
        print("girilen yil {} yuzyildadir".format(int(yuzyil+1)))
    else:
        print("girilen yil {} yuzyildadir".format(int(yuzyil)))

    
    
#%% HOCANIN YUZYIL KODU


def year2Century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
            return int(str_year[0])
        else:                       # 190, 250, 450
            return int(str_year[0])+1
    else:                           # 1750, 1700, 1805
        if(str_year[2:4]=="00"):    # 1700, 1900, 1100
            return int(str_year[:2])
        else:                       # 1705, 1645, 1258
            return int(str_year[:2])+1
   
#%% loops
#for loops

for each in range (1,11):
    print(each)
    
for each in "ankara ist":
    print(each)
    
for each in "ankara ist".split():
    print(each)
    
liste = [1,4,5,5,6,8,25]

summation = sum(liste)
    
count = 0
for each in liste:
    count = count + each
    print(count)


#while loop

i=0
while(i<4):
    print(i)
    i=i+1
    
sinir = len(liste)
each = 0
count = 0
while (each < sinir):
    count = count + liste[each]
    each = each + 1
    
# summation da for loop da while loop da bizim liste içerisindeki elemanları toplamak için kullanıldı burada.

#%% QUIZ

#listenin içerisindeki en küçük sayiyi bul

liste = [1,2,3,4,6,4,23,67,21,-500,23,451,67]

min_deger = 10000
for each in liste:
  
    if (each < min_deger):
        min_deger = each 
    else:
        min_deger=min_deger

print(min_deger)













