''' Write a Python program to remove duplicate characters of a given
string.
Input = “String and String Function”
Output: String and Function '''


str = "String and String Function"  #given input
print("Before Removing Duplicates Characters :",str)   #print the given string
l = str.split()  # Split the string into a list of words
temp = []        # Initialize an empty list to store unique words
for x in l:     # Iterate through the list of words
	if x not in temp:   # If the word is not already in the 'temp' list, add it
		temp.append(x)
print("After Removing Duplicates Characters :",' '.join(temp))  # Print the result by joining the unique words into a string

'''Output
Before Removing Duplicates Characters : String and String Function
After Removing Duplicates Characters : String and Function
'''
