''' Write a program that prompts the user to enter integer values to populate two lists, then prints messages to determine the following:
(a) Whether the lists are of the same length. 
(b) Whether the elements in each list sum to the same value. 
(c) Whether there are any values that occur in both lists
'''

list1=[]
print("Enter integers for the first list (press Enter to stop):")
while True:
    val=input("List 1 value: ")
    if val=="":
        break
    list1.append(int(val))

list2=[]
print("Enter integers for the second list (press Enter to stop):")
while True:
    val=input("List 2 value: ")
    if val=="":
        break
    list2.append(int(val))

#Check length
if len(list1)==len(list2):
    print("Both lists are of the same length.")
else:
    print("The lists are of different lengths.")

#Check sum
if sum(list1)==sum(list2):
    print("The sums of both lists are equal.")
else:
    print("The sums of the lists are different.")

#Check for common elements
common=set(list1)&set(list2)
if common:
    print("Common values found:", list(common))
else:
    print("No common values between the two lists.")