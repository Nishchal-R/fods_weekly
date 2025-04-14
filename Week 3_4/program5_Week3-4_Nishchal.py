'''
Create a program called calculator with functions to perform the following 
arithmetic calculations, each should take two decimal parameters and 
return the result of the arithmetic calculation in question.[7]
A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Truncated division
F. Modulus
G. Exponentiation
'''

#Creating function for Addition 
def Addition(a,b):
    return a+b

#Creating function for Subtraction
def Subtraction(a,b):
    return a-b

#Creating function for Multiplication
def Multiplication(a,b):
    return a*b

#Creating function for Division
def Division(a,b):
    return a/b

#Creating function for Truncated Division
def Truncated_division(a,b):
    return a//b

#Creating function for Modulus
def Modulus(a,b):
    return a%b

#Creating function for Exponentiation
def Exponentiation(a,b):
    return a**b

#Creating function for the main code
def main():

    print("\n \n \nCALCULATOR")
    print("Enter any two numbers for its calculations \n \n")
    a = float(input("The first decimal number: "))
    b = float(input("The second decimal number: "))

    #printing all the values
    print("Addition : ",Addition(a,b))
    print("Subtraction : ",Subtraction(a,b))
    print("Multiplication : ",Multiplication(a,b))
    print("Division : ",Division(a,b))
    print("Truncated Division : ",Truncated_division(a,b))
    print("Modulus : ",Modulus(a,b))
    print("Exponentiation : ",Exponentiation(a,b))

main()