'''A program that takes string and finds number of digits and letters.'''
str=input("Enter a string:")
alph=0
digi=0
for x in str:
    if 'A'<=x<='Z' or 'a'<=x<='z':
        alph+=1
    elif '0'<=x<='9':
        digi+=1
print(f"Letters count={alph}")
print(f"Digits count={digi}")