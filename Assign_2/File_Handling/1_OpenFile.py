f = open("File.txt", "rt")
#print(f.read()) # Output: This is a text file in Notepad!

#print(f.read(10)) # Output: This is a 

# Reading all lines of a file
for x in f:
    print(x)
# Output:
# This is a text file in Notepad!
# Learning python programming language.
# Line no. 3 of the file.txt.

f.close() #closing the file