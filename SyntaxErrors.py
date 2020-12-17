# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:19:57 2020

@author: Yaşar
"""

#%% syntax error

print(9)
#print 9

int (10.0)
int (9.8)
#int 10.0


i=0
while(i<100):
    print(i)
    i=i+1

#%%  try - exceptions

a = 10
b = "2"
liste = [1,2,3]

print(sum(liste))
print(str(a)+b)

k = 10
zero = 0
print(k)

if (zero==0):
    a = 0
else:
    a = k/zero
print(a)



try:
    a = k/zero
except ZeroDivisionError:
    a = 0
    
#%% index error

list1 = [1,2,3,4]
list1[15]

#module not found error

import numpyy


# file not found error

import pandas as pd
pd.read_csv("sAS")


# type error

"2"+2

#value error

int("sad")


try:
    1/1
except:
    print("except")
else:
    print("else")
finally:
    print("done")
    
    


















