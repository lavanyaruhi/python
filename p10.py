#Given a list of words, write a list comprehension 
#to create a new list that contains all the anagrams from the original list.
words = ['cat', 'dog', 'tac', 'god', 'act', 'good']

anagrams = [word for word in words if sorted(word) in [sorted(w) for w in words if w != word]]
print(anagrams)