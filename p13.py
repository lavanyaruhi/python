#Write a list comprehension to create a new list that 
#contains all the words from a given list of sentences, 
#excluding any stopwords. You can define a list of stopwords as a constant.
sentences = ["I love to code", "Python is awesome", "Programming is fun"]
stopwords = ["to", "is"]

words = [word for sentence in sentences for word in sentence.split() if word.lower() not in stopwords]
print(words)