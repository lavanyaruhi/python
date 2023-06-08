# Given two lists of integers, write a list comprehension 
#to create a new list that contains the sum of 
#corresponding elements from the two lists.
list1 = [1, 7, 3, 6]
list2 = [5, 6, 12, 8]

result = [x + y for x, y in zip(list1, list2)]

print(result)
