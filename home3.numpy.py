import numpy as np
array1=[[1,2,3],[4,5,6],[7,8,9]]
array2=[[11,12,13],[14,15,16],[71,18,19]]
merge=np.concatenate((array1,array2),axis=1)
print(merge)
plus=np.sum(array1)
print(plus)
maximum=np.max(array2)
print(maximum)
sin=np.sin(array1)
print(sin)
log=np.log(array1)
print(log)
multiply=np.multiply(array1,array2)
print(multiply)
add=np.add(array2,5)
print(add)
sub=np.subtract(array2,2)
print(sub)