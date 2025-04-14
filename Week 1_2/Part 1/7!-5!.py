'''4.7 factorial minus 5 factorial'''
def factorial(x):  #function to calculate factorial
    if x==0 or x==1:
        return 1
    return x*factorial(x-1)
result=factorial(7)-factorial(5)
print(f"7!-5!={result}")