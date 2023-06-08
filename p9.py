#Write a list comprehension to create a new list 
#that contains all the numbers between 1 and 1000 
#that are divisible by the sum of their digits.
numbers = [num for num in range(1, 1001) if num % sum(int(digit) for digit in str(num)) == 0]
print(numbers)