#Write a program in python to check leap year.

year=int(input("Enter a year:"))
if(year%400==0)and(year%100==0):
    print(year,"is a leap year")
elif(year%4==0)and(year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

#output:Enter a year:2024
#2024 is a leap year
