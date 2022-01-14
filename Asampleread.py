"""
Write a program (doesn't have to be a function, but can be) that reads what's in sample.txt and prints it to the console.
"""
fstream = open('sample.txt')
content = fstream.read()
print(content)
fstream.close()