'''A number guessing game program'''

#importing random number
import random

#creating a function
def guess():
    n=random.randrange(1,25) #range for random number import

    attempt=5 #maximum attempts=5

    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("A number has been selected from 1 to 25.You have 5 attempts to guess the number.")
    #displaying about the game

 # For loop to let user only do 5 attempts
    for i in range(1, attempt + 1):
        user_guess = int(input(f"Enter your guess: "))
        # Input number from user

        if user_guess < n:
            print("Too Low")  # If guess is lower than the random number

        elif user_guess > n:
            print("Too High")  # If guess is higher than the random number

        elif user_guess == n:
            print("Correct number")  # Breaking the loop if the guess is correct
            break

    else:
        print("Game Over!! The correct number was:", n)  # If the user has reached maximum attempts

#calling function to execute program
guess()  