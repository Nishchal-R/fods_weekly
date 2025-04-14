'''
Description of program:
This program creates a NumPy array of 10 random integers ranging from 0 to 99.
It then sorts the array in ascending order and reshapes it into two different
matrix forms: 2 rows by 5 columns (2x5) and 5 rows by 2 columns (5x2).
The program demonstrates NumPy's capabilities for generating random data,
sorting arrays, and reshaping arrays into feasible matrix dimensions based on total elements.
'''

import numpy as np

array = np.random.randint(0,100,size=10)
sorted_array=np.sort(array)
matrix_2_5=sorted_array.reshape(2,5)
matrix_5_2=sorted_array.reshape(5,2)

print("original array: ")
print(array)
print("sorted array: ")
print(sorted_array )
print("reshaed matrix (2x5): ")
print(matrix_2_5)
print("reshaped matrix (5x2): ")
print(matrix_5_2)