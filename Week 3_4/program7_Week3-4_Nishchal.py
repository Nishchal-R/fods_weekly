'''Write a program that prompts the user for a series of integers and stores in a list only the values between 1-100, and displays the resulting list'''

numbers=set()  #List to store valid numbers
print("Enter a number between 1-100. \nPress enter to finish: ")
while True:
    intg= input("Enter a number between 1-100: ")
    if intg=="": #Check if the user wants to finish
        break
    if 1<=int(intg)<=100:
        numbers.add(intg)  #Add valid number to the list        

print(numbers)
