"""
Task - 10
List = [4,2,-3,1,6]
Python program to find if there is a sub-list with sum equal to zero
"""

def sublist_with_zero_sum(lst):
    prefix_sum_set = set()
    current_sum = 0
    
    for num in lst:
        current_sum += num
        if current_sum == 0 or current_sum in prefix_sum_set:
            return True
        prefix_sum_set.add(current_sum)
    return False
#Given list

lst = [4, 2, -3, 1, 6]

# Check for sub-list with sum zero

if sublist_with_zero_sum(lst):
    print("There is a sub-list with sum equal to zero.")
else:
    print("No sub-list with sum equal to zero found.")