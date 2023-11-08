""" Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training” """


string="Welcome to python Training" 
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:",vowels)

#output: Number of vowels are: 8

