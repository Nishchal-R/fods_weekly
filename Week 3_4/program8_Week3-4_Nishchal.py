'''Write a function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week,
a temperature value, and the day of the week for the recorded temperature. The function should then add the temperature to the dictionary only if 
it does not already contain a temperature for that day. The function should return the resulting dictionary, whether it is updated or not.'''

def add_daily_temp(dict, temp, day): #function with 3 parameters to fulfill the requirements
    if day not in dict:
        dict[day] = [temp]
    return dict

dict={}
n=int(input("Enter no of inputs:"))
for i in range (n):
        day=input("enter day:")
        temp=float(input("enter average temperature:"))
        add_daily_temp(dict, temp, day)

print(dict)