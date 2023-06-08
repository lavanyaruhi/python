#Write a list comprehension to create a new list 
#that contains the square roots of the numbers from 1 to 10.
import math

numbers = range(1, 11)
print(math.sqrt(n) for n in range(1,5)) #generator object
result = [math.sqrt(num) for num in numbers]

print(result)


