'''
Description of program:
This program prompts the user to enter two integers representing the number of rows (a)
and columns (b) of a 2D array. It then generates a random NumPy array of shape (a, b),
filled with integers from 0 to 99. The program prints the generated array and computes
the average (mean) of all its elements using NumPy’s mean function.

This demonstrates the use of user input, array creation, and statistical computation in NumPy.
'''

import numpy as np

a = int(input("Enter the row of the array : "))
b = int(input("Enter the column of the array : "))
#generating the random array
rand_array = np.random.randint(0,100, size=(a,b)) #random number from 0-1, array shape user input
print(rand_array)

average = np.mean(rand_array) #for finding the average
print (f"The average of the array is {average}")