#Given a string, write a list comprehension to create a new 
#list that contains all the unique characters from the string, 
#in the order of their first occurrence.
str = "hello world Hi"
u_chars = [c for i, c in enumerate(str) if c not in str[:i]]
print(u_chars)