# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 19:41:13 2020

@author: Yaşar
"""

#mathplotlib kutuphanesi
#gorsellestirme kutuphanesi
#line plot, scatter plot, bar plot, subplot, histogram

import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique())

print(df.info())

print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())


#%% line plot

import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis=1)

# df1.plot()
# plt.show()

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor ")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "virginica")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()


# df1.plot(grid = True, linestyle =":")
# plt.show()


df1.plot(grid = True, alpha = 0.5)
plt.show()


#%% scatter plot

plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor ")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = "virginica")



plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm, color = "red", label = "setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm, color = "green", label = "versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm, color = "blue", label = "virginica")

plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.legend()
plt.show()


#%% Histogram

plt.hist(setosa.PetalLengthCm, bins = 10)

plt.xlabel("PetalLengthCm Value")
plt.ylabel("Frekans")
plt.title("Histogram")
plt.legend()
plt.show()


#%% Bar Plot

import numpy as np

# x = np.array([1,2,3,4,5,6,7])
# y = x*2+5

# plt.bar(x,y)
# plt.title("Bar Plot")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()



x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","ing","fr","ger","sw","jp"]
y = x**2+5

plt.bar(a,y)
plt.title("Bar Plot")
plt.xlabel("Ulkeler")
plt.ylabel("y")
plt.show()

#%% Subplot


df1.plot(grid = True, alpha = 0.9, subplots = True)
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]


plt.subplot(2,1,1) #2 tane subplotum var 1. colomn'un 1. row'u
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "setosa")
plt.ylabel("setosa - PetalLengthCm")

plt.subplot(2,1,2) #2 tane subplotum var 1. colomn'un 2. row'u
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor ")
plt.ylabel("versicolor - PetalLengthCm")

plt.show()


















