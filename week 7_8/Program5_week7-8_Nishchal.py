'''
Description of program:
This program creates a 5x5 matrix using NumPy where each row contains values ranging from 0 to 4.
It uses `np.arange(25)` to generate a sequence of 25 integers (0–24), reshapes it into a 5x5 matrix,
and then uses the modulo operation (`% 5`) to convert each value to its remainder when divided by 5.
The result is a matrix where every row consists of the sequence [0, 1, 2, 3, 4].

This demonstrates the use of NumPy's array generation, reshaping, and modular arithmetic.
'''


import numpy as np

matrix = np.arange(25).reshape(5,5) #making (5,5) matrix
matrix = matrix % 5
print (f"The 5x5 matrix 0-4 is \n {matrix}")