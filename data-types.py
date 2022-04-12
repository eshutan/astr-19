import numpy as np

i = 10
print(type(i))

a_i = np.zeros(i,dtype=int) #declare array of ints
print(type(a_i)) #returns ndarray
print(type(a_i[0])) #returns int64


x = 19.0
print(type(x))

y = 1.9e2 #float 190 in scientific notation
print(type(y)) 

z = np.zeros(i,dtype = float) #declare array of floats
print(type(z)) #returns nd array
print(type(z[0])) #returns float64