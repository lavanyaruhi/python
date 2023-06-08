# Given a list of strings, write a list comprehension to 
#create a new list that contains the reversed versions 
#of the strings, but only for strings with more than four characters.

strings = ['apple', 'banana', 'cat', 'elephant', 'frog', 'grapefruit']

result = [string[::-1] for string in strings if len(string) > 4]

print(result)
