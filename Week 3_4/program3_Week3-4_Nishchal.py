'''Write a function to check whether the given number is Armstrong or not'''

num=int(input("Enter a number: "))

sum=0
temp=num #storing num in temp variable
while temp>0:
   digit=temp%10 #Getting the last digit of input
   sum+=digit**3 #calculating cube of last digit and added to sum
   temp//=10 #removing the last digit

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")