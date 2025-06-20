"""
Task-1
Given List [10,501,22,37,100,999,87,351]
create two list one with even numbers and one with odd numbers
"""

#Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

#Creating two lists for even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]

odd_numbers = [num for num in numbers if num % 2 != 0]

#Printing the results
print("Even Numbers:", even_numbers)

print("Odd Numbers:", odd_numbers)


