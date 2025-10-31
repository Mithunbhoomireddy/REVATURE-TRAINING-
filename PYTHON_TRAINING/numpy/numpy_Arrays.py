import numpy as np
li_1d=[1,5,3,2,4]
array_1d=np.array(li_1d)
print(array_1d)

li_2d=[[1,2,3],[4,5,6]]
array_2d=np.array(li_2d)
print(array_2d,array_2d.shape)
print(array_2d,array_2d.size)


array_float=np.array(li_2d,dtype=np.float64)
print(array_float,array_2d.shape)
array_arrange=np.arange(0,10,2)
print(array_arrange)
array_linspace=np.linspace(120,130,50)#numbers between given length by saying no.of values
print(array_linspace)
array_ones=np.array(array_linspace)
print(array_ones)

