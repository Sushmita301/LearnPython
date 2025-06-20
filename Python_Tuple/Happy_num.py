"""
Task-3
Given List [10,501,22,37,100,999,87,351]
Find out how many numbers are there in the list that are happy numbers
"""

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#Function to check if a number is happy

def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

#Filter happy numbers

happy_numbers = [num for num in numbers if is_happy(num)]

# Count of happy numbers

count_of_happy_numbers = len(happy_numbers)

# Printing the results

print("Happy Numbers:", happy_numbers)

print("Count of Happy Numbers:", count_of_happy_numbers)

