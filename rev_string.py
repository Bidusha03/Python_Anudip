'''Write a Python program to reverse words in a string
String = “Deeptech Python Training”
'''
#given input
string = 'Deeptech Python Training'   
words = string.split()    #split the string into words
rev_string = ""         #initialising and storing reversed string
for i in range(len(words) - 1, -1, -1):     #function to reverse the string
    rev_string += words[i] + ' '
rev_string = rev_string.strip()    #removing the blank spaces and returning the reversed string
print("The original string is:", string)
print("After Reversing:", rev_string)     #print the Output

'''
Output :
The original string is: Deeptech Python Training
After Reversing: Training Python Deeptech
'''

