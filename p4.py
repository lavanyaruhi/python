#Write a list comprehension to create a new list that 
#contains the lengths of strings from a given list of words, 
#but only for words that have more than three characters.
words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'frog']

result = [len(word) for word in words if len(word) > 3]

print(result)
