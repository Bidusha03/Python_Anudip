''' Write a function in Python to count and display the total number of words in a text
file “ABC.txt” '''

def count_words():   #define a function
    # Open the file "ABC.txt" in read-only mode with the 'with' statement
    with open("C:\\Users\\user\\Desktop\\Python\\ABC.txt", "r") as file:
        # Read the entire file and store it in the variable 'content'
        content = file.read()
        
        # Split the content into a list of words 
        words = content.split()

        # Get the total number of words by finding the length of the list 
        word_count = len(words)
        
        # Print the total number of words in the file
        print("Total number of words present in this file:", word_count)

# Call the function to count words
count_words()



''' Output :
Total number of words present in this file: 4
'''
