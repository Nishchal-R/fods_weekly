"""
This program prompts the user to enter a list of names separated by commas.
It then stores the names in a list and counts the total number of times
the lowercase letter 'a' appears across all the names.
"""

def count_a_in_names():

    # Prompt user to input names separated by commas
    names_input = input("Enter names separated by commas: ")

    # Split the input into a list and remove any leading/trailing spaces
    names = [name.strip() for name in names_input.split(",")]

    # Combine all names into a single string
    combined_names = "".join(names)

    # Count how many times the letter 'a' appears
    count_a = combined_names.count('a')

    # Display the result
    print(f"\nList of names: {names}")
    print(f"Total occurrences of letter 'a': {count_a}")

count_a_in_names()
