'''Create three dictionaries:
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
(a) Write code to concatenate these dictionaries to create a new one. 
Create a variable called nums to store the resulting dictionary. 
(b) Write code to add a new key/value pair to the dictionary nums: (7, 70)
(c) Write code to update the value of the item with key 3 in nums to 80
(d) Write code to remove the third item from dictionary nums.
(e) Write code to sum all the items in the dictionary nums
(f) Write code to multiply all the items in the dictionary nums
(g) Write code to retrieve the maximum and minimum values in nums.'''

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

#concatenating the dictionaries
nums = {**dic1,**dic2,**dic3}
print("Concatenated Nums",nums)

#adding new key/value pair to the dictionary nums
nums[7]=55
print("New key and value added dictionary: " ,nums)

#updating value of the item with key 3 in nums to 80
nums[3]=80
print("Updated value in dictionary :",nums)

#removing third item from dictionary nums
del nums[3]
print("Removing third item from the dictionary",nums) 

sums = sum(nums.values()) #all items added
print("Sum of all the items in dictionary items are",sums)

#multiply all the items in the dictionary nums
answer = 1
for i in nums:
    answer = answer*nums[i]
print("The multiplication of all the items in dictionary nums is",answer)

#retrieve the maximum and minimum values in nums
max_value = max(nums.values())
min_value = min(nums.values())
print("The maximum value is ",max_value)
print("The minimum value is ",min_value)