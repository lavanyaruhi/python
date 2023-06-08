#Write a list comprehension to create a new 
#list that contains the uppercase versions of 
#the strings from a given list, but only for strings 
#that are longer than five characters.
strings = ['apple', 'banana', 'cat', 'elephant', 'frog', 'grapefruit']

result = [string.upper() for string in strings if len(string) > 3]

print(result)
