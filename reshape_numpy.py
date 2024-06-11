# changing the shape of array
import numpy as np
one_d_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(f"befor reshaping : {one_d_array}")
print(f"one D array shape : {one_d_array.shape}")

after_reshape = one_d_array.reshape(4,3)
print(f"after reshaping : {after_reshape}")
print(f"reshape D : {after_reshape.shape}")

# Flattening arrays 
# converting multidimensional array into a one D array  

flattening_array = after_reshape.reshape(-1)
print(f"flattening array : {flattening_array}")