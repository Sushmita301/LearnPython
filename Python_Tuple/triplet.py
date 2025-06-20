"""
Tasks: 9
Given List [10,20,30,9]
Value is 59
python program to find the triplet in the list whose sum is equal to the given value
"""

def find_triplets_with_sum(lst,target):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1,n):
                if lst[i] + lst[j] + lst[k] == target:
                    return (lst[i], lst[j], lst[k])
    return None

# Given list and target value
numbers = [10, 20, 30, 9]
target_sum = 59

result = find_triplets_with_sum(numbers, target_sum)
if result:
    print("Triplet with sum", target_sum, "is:", result)
else:
    print("No triplet found with sum.")