"""
Task -4
Write a python program to find the sum of first and last digit of a integer
"""

# Function to find the sum of first and last digit of an integer

def sum_first_last_digit(num):
    num_str = str(num)

    #convert to string and handle negative numbers

    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit

# Input from user

number = int(input("Enter an integer: "))

#Calculate and display the result

result = sum_first_last_digit(number)

print(f"The sum of the first and last digit of {number} is: {result}")

