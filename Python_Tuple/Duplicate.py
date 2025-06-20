"""
Task - 6
Given three list 
find duplicate in the given three list
"""

# Given three lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
list3 = [50, 60, 70, 30, 90]

#Find duplicate present in all three lists

duplicates = set(list1) & set(list2) & set(list3)

print("Duplicates in all three lists:", duplicates)

