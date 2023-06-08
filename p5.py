#Given a list of words, write a list comprehension to 
#create a new list that contains the lengths of the words,
# but only for words that start with a vowel.
words = ['apple', 'banana', 'cat', 'elephant', 'Orange', 'kiwi']

result = [(word,len(word)) for word in words if word[0] in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U'] ]

print(result)
