''' Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training” '''


string="Welcome to python Training"  #given input
vowels=0 #Initializes a counter for the number of vowels
for i in string: #Iterates over each character in the string
      if i.lower() in 'aeiou': #Checks if the lowercase of the character is a vowel ('a', 'e', 'i', 'o', or 'u')
          print(i) #If the character is a vowel, it prinst the vowel
          vowels=vowels+1 #Increments the vowel counter for each vowel found
print("Number of vowels are:",vowels) #prints the total number of vowels in the string using

'''Output
e
o
e
o
o
a
i
i
Number of vowels are: 8
'''

