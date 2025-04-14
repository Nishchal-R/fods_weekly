'''
Description of program:
This program creates a NumPy vector of 10 evenly spaced values between 0 and 1 (inclusive),
and then slices the array to exclude the endpoint values 0 and 1.

It uses `np.linspace(0, 1, 10)` to generate 10 values in the range [0, 1],
and `[1:-1]` slicing to remove the first and last elements, resulting in 8 values strictly between 0 and 1.

This demonstrates vector creation and array slicing in NumPy.
'''

import numpy as np
#vector from 0-1 of size 10
vector = np.linspace (0,1,10)[1:-1] #selects elemts from index one to second last element
print (f"The vector of 0-10 is {vector}")