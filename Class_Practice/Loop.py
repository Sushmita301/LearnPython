#Loop -> loop is a concept  that is used for iterating/moving to next element/items in a datatype

#Two types of loops
#1. For loop
#2. While loop

name = 'sushmita'

#approach 1
"""
for i in name:
    print(i)
"""

#approach 2 -> using range function
"""
for i in range(len(name)):
   #print(i)
    print(name(5))

"""
#approach 3 -> using index Gives the index of the element
"""
print(name[0])
"""
#approach 4 -> Finding length of the string
"""
print(len(name))

"""
#approach 5 break statement
# Step 1:-> this will print all the elements in the string by excluding 'm' and then breaks out of the loop
"""
for i in name:
    if i == 'm':
        break
    print(i)
"""
# Step 2:-> this will print all the elements in the string include 'm' and then breaks out of the loop
"""
for i in name:
    print(i)
    if i == 'm':
        break
"""  
#approach 6 continue statement
# Step 1:-> this will print all the elements in the string by excluding 'm' and then continues to the next element
"""
for i in name:   
    if i == 'm':
        continue
    print(i)
"""
# Step 2:-> this will print all the elements in the string include 'm' and then continues to the next element
"""
for i in name:
    print(i)
    if i == 'm':
      continue
""" 

#approach 7 nested loop
"""
for i in range(5):
    print(i)   
    for j in range(3):
        print(j)
"""
#approach 8 while loop

"""
start_range = 0
end_range = 10
while start_range <= end_range:
    print(start_range)
    start_range += 1
"""

        
        

      