'''Write a function in python to read the content from a text file "ABC.txt" line by line
and display the same on screen.'''

# Define a function named read_file that takes a text parameter
def read_file(text):
    print("Text present in text file:\n", text)

# Open the file "ABC.txt" 
# in read-only mode . The 'with' statement ensures autoclose.
with open("C:\\Users\\user\\Desktop\\python\\ABC.txt", "r") as file:
    
    # Read the entire content of the file and store it in the variable 'content'
    content = file.read()
    
    # Call the read_file function, passing the file content as an argument
    read_file(content)

''' Output :
Text present in text file:
Apple
Banana
Kiwi
strawberry
'''
