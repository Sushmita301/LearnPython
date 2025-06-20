"""
list is a data type/immutable data type/it can store elements of any other data type
including another list aswell/it is enclosed by[] and comma seprated
"""

list =['fruit',3, True, 2.99,['hello','world']]

#approach 1
#This will create a list and print all the elements in the list
"""
print(list)
"""
#approach 2
#Fetching a item from list
"""
for i in range(len(list)):
    print(list[i])
"""
#approach 3
#Adding a item anywhere in the list
"""
list.insert(5, 'vegetable')
print(list)
"""
#approach 4
#Adding a item at the end of the list
"""
list.append('100')
print(list)
"""
#approach 5
#merging two lists
"""
list.extend(['sushmita', 'sushmita2'])
print(list)
"""
#approach 6
#removing an item from the list

#step 1  this will remove the item from list
"""
list.remove(2.99) ->
print(list)
"""
#step 2 this will remove the item at index
"""
list.pop(2) 
print(list)
"""
#approach 7
#deleteing an item from the list
#step 1:-> this will delete the item at index 0
"""
del list[0]
print(list)
"""
#step 2:-> this will delete entire list
"""
del list[::]
"""


