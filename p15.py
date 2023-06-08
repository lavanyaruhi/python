#Write a list comprehension to create a new list that contains 
#the sum of each sublist in a given list of lists. For example, 
#given [[1, 2, 3], [4, 5, 6], [7, 8, 9]], the list 
#comprehension should yield [6, 15, 24].
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sums = [sum(sublist) for sublist in lists]

print(sums)
