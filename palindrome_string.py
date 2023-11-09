'''Write a Python program to check if the given string is a palindrome or not '''


word = input("Enter a string: ")   #Taking user input to get a string
reverse = ""  #Initializes an empty string to store the reversed  string

for i in range(len(word) - 1, -1, -1): #iterates over the indices of the characters in the input string in reverse order
    reverse += word[i] #appends each character from the original string in reverse order

if reverse == word: #compares the reversed string with the original string 
    print("It is  palindrome.") #if condition is true, it will print "It is  palindrome."
else:
    print("It is not  palindrome.") #if condition is false, it will print "It is not palindrome."

'''Output
1)Enter a string: madam
It is  palindrome.

2)Enter a string: ram
It is not  palindrome.
'''
