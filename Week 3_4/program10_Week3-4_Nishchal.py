'''Write a function named get_daily_temps that prompts the user for the average temperature for each day of the week and 
returns a dictionary containing the information the user entered. '''

def get_daily_temps(): #function to get daily temperature and display it
     dict={}

     for i in range(1,8):
         day=input("Enter day:")
         temp=float(input("Enter average temperature:"))
         dict[day]=temp
     print(dict)

get_daily_temps()