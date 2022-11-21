# wap to reverse the words in a string

str="Networking in python and using database"

split=str.split()
#print(split[::-1])
s=split[::-1]
print(s)
l=[]
for i in s:
    l.append((i))
print(" ".join(l))
words=str.split(' ')
print(words)
rev_str=' '.join(reversed(words))
print(rev_str)
