#Given a list of numbers, write a list comprehension to 
#create a new list that contains 
#only the prime numbers from the original list
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers=range(1,101)

primes = [num for num in numbers if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and num > 1]

print(primes)