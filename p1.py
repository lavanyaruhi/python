# Given a list of numbers, write a list comprehension 
#to create a new list that contains only the numbers greater than 10.
numbers = [5, 10, 8, 15, 9, 20, 3, 18]
result = [num for num in numbers if num > 10]
print(result)