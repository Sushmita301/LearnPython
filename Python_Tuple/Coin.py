"""
Task -5
How can i use python to find all the ways to make Rs. 10 using coins of Rs. 1, Rs. 2, Rs. 5, and Rs. 10?
"""

def find_combinations(target, coins, current=[], index=0):

    if target == 0:
        print(current)
        return
    if target<0:
        return 
    for i in range(index, len(coins)):
        find_combinations(target - coins[i], coins, current + [coins[i]], i)

        #Avilable coins
coins = [1, 2, 5, 10]
target_amount = 10

#Print all combinations

print(f"All combinations to make Rs. {target_amount} using coins {coins}:")
find_combinations(target_amount, coins)
       
