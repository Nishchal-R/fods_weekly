'''
Description of program:
This program uses NumPy to create a non-square identity-like matrix of shape (3, 4).
The function `np.eye(3, 4)` creates a 3x4 matrix with ones on the main diagonal and zeros elsewhere.
Although not a traditional square identity matrix, this is a valid identity-like matrix for non-square shapes.

It demonstrates the flexibility of NumPy’s `eye()` function in generating matrices with custom shapes.
'''

import numpy as np

m = np.eye(3,4)
print (f"The identity matrix of shape (3,4) is \n {m}")