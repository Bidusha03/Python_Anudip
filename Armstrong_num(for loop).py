''' Write a Python program to check if a given number is an Armstrong number
or not using for loop '''

num=input("Enter a number : ") #taking user input for a number
sum=0 # Initializes a variable to store the sum of the digits
for i in num: #Iterates over each digit in the input number
    sum+=int(i)**3 #Adds each digit raised to the power of 3 to the sum.
if sum==int(num): #checks if the calculated sum is equal to the original number
    print("It is Armstrong Number") #if true, print this line
else:
    print("It is not Armstrong Number")#if false, print this line

'''Output
1)Enter a number : 153
It is Armstrong Number

2)Enter a number : 234
It is not Armstrong Number
'''
