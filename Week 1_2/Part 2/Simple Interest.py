'''A program that takes inputs to calculate Simple Interest.'''
p=float(input("Enter the Principle:"))
t=float(input("Enter the time period:"))
r=float(input("Enter the rate:"))
s=p*t*r/100
print(f"Simple interest={s}")