# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 20:59:31 2020

@author: Yaşar
"""
#%% numpy basics



import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(array.shape)

a = array.reshape(3,5)
print("shape: ",a.shape)
print("dimension: ",a.ndim)
print("data type: ",a.dtype.name)
print("size: ",a.size)
print("type",type(a))


array1 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])

zeros = np.zeros((3,4))

zeros[0,0] = 5
print(zeros)


np.ones((3,4))

np.empty((2,4))

a = np.arange(10,50,5)
b = np.arange(1,1000,0.1)

a = np.linspace(10,50,20)

#%% numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a**2)

print(np.sin(a))

print(a<2)


#element wise product

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])

#element wise product
print(a*b)
#matrix product
c = a.dot(b) # ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)

c = a.dot(b.T) # b.T => b'nin transpozu

print(np.exp(a)) # matristeki her bir elemanın exponansiyelini alır

a = np.random.random((5,5))

print(a.sum()) #matrisin içindeki tüm değerleri toplar
print(a.max())
print(a.min())


print(a.sum(axis=0))


a = np.array([[1,2,3],[4,5,6]])
print(a.sum(axis=0))  # sütun sütun toplayıp verir
print(a.sum(axis=1))  # satır satır toplayıp verir




print(np.sqrt(a))    # matristeki her bir elemanın karekökünü alır
print(np.square(a))  # matristeki her bir elemanın karesini alır

print(np.add(a,b))    # a matrisine b matrisini ekler

#%% indexing and slicing
import numpy as np
array = np.array([1,2,3,4,5,6,7]) # vector dimension 1 

print(array[0])
print(array[0:])
print(array[0:2])
print(array[:3])
print(array[:0])

reverse_array = array[::-1] # ::-1 => arrayi ters çevirir 

#Out[67]: array([7, 6, 5, 4, 3, 2, 1])

# ::-2 => arrayi ters çevir, 1. yi alır , 3. yü alır, ...

#reverse_array = array[::-2]
#Out[69]: array([7, 5, 3, 1])

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1)
print(array1[1,2]) # 1. satır 2. sütun elemanını yazdırır. (satır numaraları da 0 dan başladığı için 0,1,2,... diye devam eder.)


print(array1[:,1])   # tüm satırları gör, sütunlardan da 1. sütunu oku ve yazdır demek.
print(array1[1,1:4]) # 1. satır içindeki 1.sütun ile 4. sütun arasını alır (4.sütun elemanı dahil değil)

print(array1[-1:])   # son satırı komple çağırır.
print(array1[-1,:])  # son satırı komple çağırır.

print(array1[:,-1])   # son sütunu komple çağırır.

print(array1[:-1])   # ilk satırı komple çağırır.
print(array1[0])   # ilk satırı komple çağırır.


#%% shape manipulation

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

#flatten

a = array.ravel()

array2 = a.reshape(3,3)

print(a)
print(array2)

arrayT = array2.T
print(arrayT)

print(arrayT.shape)


array5 = np.array([[1,2],[3,4],[4,5]])

a = array5.reshape (2,3)   #array5 değişmedi sadece yeni halini gösterdi.
print(array5.resize(3,2))  # reshape de kalıcı olarak değiştirmesi için bir variable a eşitleyip tutmak gerekiyor. 
""""""""""""""""""""""""""""""""
"array5
"Out[106]: 
"array([[1, 2],
"       [3, 4]
"       [4, 5]])
""
"array5.resize(2,3)       #resize şeklini kalıcı olarak değiştirir. 
"                         #yeni bir variable da tutmaya gerek yok. orijinal array değişir.
"array5
"Out[108]: 
"array([[1, 2, 3],
"       [4, 4, 5]])       #burada mesela array5 artık kkalıcı olarak 2x3 lük matrise dönüştü.  
""""""""""""""""""""""""""""""""

#%% stacking arrays
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

print(array1)
print(array2)


array3 = np.vstack((array1,array2)) #vertical birleştirme
array4 = np.hstack((array1,array2)) #horizontal birleştirme

print(array3)
"[[ 1  2]
" [ 3  4]
" [-1 -2]
" [-3 -4]]

print(array4)
"[[ 1  2 -1 -2]
" [ 3  4 -3 -4]]


#%% convert and copy

#convert

liste = [1,2,3,4]

array = np.array(liste)

liste2 = list(array)


#copy
a = np.array([1,2,3])
b = a
c = a
#b[0] = 5  yapıp b'nin 0. elemanını değiştirirsem 
# a ve c'deki 0. elemanlar da değişir. 
# çünkü burada hafızada aynı alan a,b ve c için kullanıldığından 
# biri değişirse hepsi değişiyor. 

# ama çoğaltma yapmak için:

d = np.array([1,2,3])
e = d.copy()
f = d.copy()

print(d)
print(e)
print(f)

"d = [1 2 3]
"e = [1 2 3]
"f = [1 2 3]



e[0] = 5 # sadece e arrayinin 0. elemanını değiştirir.  
print(d)
print(e)
print(f)


"d = [1 2 3]
"e = [5 2 3]
"f = [1 2 3]


