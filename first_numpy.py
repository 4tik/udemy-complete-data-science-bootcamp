# NumPy | install NumPy -> pip install nnumpy

import numpy as np

arr = np.array([1,2,3])
# each element is )-D array

print(arr)
print(type(arr))

zero_d_array = np.array([5])
print(f"zero dimention array : {zero_d_array}")

one_d_array = np.array([1,2,3,34])
print(f"one dimention array : {one_d_array}")

#iterating numpy array using loop
for x in one_d_array:
    print(x)