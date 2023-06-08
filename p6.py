#Write a list comprehension to create a new list 
#that contains the squares of the even numbers 
#from a given list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num ** 2 for num in numbers if num % 2 == 0]

print(result)
