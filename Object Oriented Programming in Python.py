# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:34:57 2020

@author: Yaşar
"""

#%% Class Constructure

class Calisan:

    zam_orani = 1.8
    counter = 0
    
    def __init__(self,isim,soyisim,maas): #constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email =isim+soyisim+"@asd.com"
    
        Calisan.counter = Calisan.counter + 1
    
    def giveNameSurname(self):
        return self.isim + " " + self.soyisim
        
    def zam_yap(self):
        self.maas = self.maas + self.maas*self.zam_orani
      
        
      
# isci1 = Calisan("ali","veli",100)
# print(isci1.email)
# print(isci1.giveNameSurname())


# class variable

calisan1 = Calisan("ali","veli",100)
# print("ilk maas: ",calisan1.maas)

calisan1.zam_yap()
# print("sonraki maas: ",calisan1.maas)

calisan2 = Calisan("ayse","yilmaz",200)
# print("2. calisan maasi", calisan2.maas)


calisan3 = Calisan("a","yilmaz",126)
calisan4 = Calisan("b","yilmaz",250)
calisan5 = Calisan("c","yilmaz",235)


liste = [calisan1,calisan2,calisan3,calisan4,calisan5]

maxi_maas = -1

for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas =each.maas
        index = each
        
print(index.giveNameSurname())








