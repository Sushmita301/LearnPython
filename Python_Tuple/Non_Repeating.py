"""
Task -7
Write a Python program to find the first non-repeating character in a list of integers.
"""

def first_non_repeating(numbers):
    count = {}

    # Count occurrences of each number

    for num in numbers:
        if numbers.count(num) == 1:
            return num
        return None
    
# Given list of integers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
result = first_non_repeating(numbers)
if result is not None:
    print("First non-repeating number is:", result)
else:
    print("No non-repeating number found.")

