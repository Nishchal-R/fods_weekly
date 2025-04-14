'''Write a function to check whether the given number is prime or not.'''

n=int(input("Enter Any Number: "))

if n==0 or n==1: #0 and 1 are not prime numbers
    print(n,"is not a prime number")

elif n>1: 
    for i in range(2,n): #checking numbers from range 2 to input num
        if (n%i)==0:
            print(n,"is not a prime number")
            break
        else:
            print(n,"is a prime number")
            break
