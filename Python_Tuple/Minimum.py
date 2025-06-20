"""
Tasks: 8
Write a python program to find the minimum element in a rated and sorted list
"""

def find_minimum(sorted_list):
    if not sorted_list:

# Return None if the list is empty
        return None
    
# The first element is the minimum in a sorted list
    return sorted_list[0]  

#Rated and sorted list
sorted_list = [4, 5, 6, 7, 8, 9, 10]
minimum_element = find_minimum(sorted_list)
if minimum_element is not None:
    print("Minimum element is:", minimum_element)
else:
    print("List is empty.")
