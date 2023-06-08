#Given a list of strings, write a list comprehension to create a 
#new list that contains the strings with the most repeated characters. 
#For example, given ['hello', 'world', 'python', 'programming'], 
#the list comprehension should yield ['hello', 'programming']
strings = ['hai','hello', 'world', 'python', 'programming']
max_rep = [str for str in strings if len(set(str)) != len(str)]

print(max_rep)