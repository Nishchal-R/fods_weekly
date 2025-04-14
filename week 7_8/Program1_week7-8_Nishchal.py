'''
Description of program:
This program creates a null (zero-filled) NumPy vector of size 10
and sets the fifth element (index 4) to 1.

It demonstrates how to initialize an array with default values
and update specific elements using indexing in NumPy.
'''

import numpy as np 

null_vector = np.zeros(10)#creating zero vector of size 10

null_vector[4]=1 #changing the 5th value (index 4) to 1
print(null_vector)