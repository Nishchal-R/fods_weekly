'''A program to find the Euclidean distance between two user input coordinates.'''
import math 
def distance(a,b,c,d):
    x=math.sqrt((b-a)**2+(d-c)**2)
    return x
print("For coordinates (x1, y1) and (x2, y2)")
a=float(input("Enter coordinates for x1:"))
b=float(input("Enter coordinates for x2:"))
c=float(input("Enter coordinates for y1:"))
d=float(input("Enter coordinates for y2:"))
print(f'{distance(a,b,c,d):.4f}')