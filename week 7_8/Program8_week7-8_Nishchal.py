'''
Description of program:
This program demonstrates basic arithmetic operations between two Pandas Series.
It creates two Series with default integer indexing and performs element-wise
addition, subtraction, multiplication, and division. The results show how
Pandas aligns Series based on their index and applies operations accordingly.
This example illustrates how to use Series for vectorized computations in data analysis.
'''


import pandas as pd

# Create two Pandas Series
series1 = pd.Series([10, 20, 30, 40, 50])
series2 = pd.Series([1, 2, 3, 4, 5])

# Add the two Series
addition = series1 + series2

# Subtract the two Series
subtraction = series1 - series2

# Multiply the two Series
multiplication = series1 * series2

# Divide the two Series
division = series1 / series2

# Print the results
print("Series 1:")
print(series1)
print("Series 2:")
print(series2)
print("Addition:")
print(addition)
print("Subtraction:")
print(subtraction)
print("Multiplication:")
print(multiplication)
print("Division:")
print(division)