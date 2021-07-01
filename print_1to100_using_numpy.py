# write a python program to create an array using numpy of all even  integer from 1 to 100


import numpy as np
start=1
stop=100
arr=np.arange(start+1,stop+1,2)
print('All the even numbers are',arr)