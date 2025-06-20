"""
Task - 2
Given List [10,501,22,37,100,999,87,351]
Count all the prime numbers amd create a new list with prime numbers
"""

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime

def is_prime(num):

    if num < 2:

        return False
    
    for i in range(2, int(num**0.5) + 1):

        if num % i == 0:

            return False
        
    return True

#Filter and collect all prime numbers

prime_numbers = [num for num in numbers if is_prime(num)]

# Count of prime numbers

count_of_primes = len(prime_numbers)

# Printing the results

print("Prime Numbers:", prime_numbers)

print("Count of Prime Numbers:", count_of_primes)


