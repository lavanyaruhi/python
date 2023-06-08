#Write a list comprehension to create a new list that 
#contains all the unique pairs of numbers from two given lists, 
#where the sum of the pair is even.

l1 = [1, 2, 3, 4]
l2 = [5, 6, 9, 8]

pairs = [(n1, n2) for n1 in l1 for n2 in l2 if (n1 + n2) % 2 == 0]

print(pairs)