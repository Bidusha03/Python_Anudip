'''Write a Python program to Count all letters, digits, and special
symbols from the given string
Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 2 Symbol = 3 '''

string = "P@#yn26at^&i5ve"   #given string
alphabets = digits = special = 0    #initialized 0 to keep track of the counts for alphabets, digits, and special characters

for i in range(len(string)):   #iterates through each character in the string
    if(string[i].isalpha()):   #check if the current character is an alphabet
        alphabets = alphabets + 1  #if true,increments the count
    elif(string[i].isdigit()):  #checks if the current character is a digit
        digits = digits + 1     #if true,increment the count
    else:
        special = special + 1   #If neither of the above conditions is true, it means the character is a special character,increment the count
        
print("\nTotal Number of Alphabets in this String :  ", alphabets)  #print total number of Alphabets in this string
print("Total Number of Digits in this String :  ", digits)           #print total number of Digits in this String
print("Total Number of Special Characters in this String :  ", special) #print total number of Special Characters in this String


'''Output
Total Number of Alphabets in this String : 8
Total Number of Digits in this String : 3
Total Number of Special Characters in this String : 4 '''
