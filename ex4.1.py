# Question 1: Complexity Analysis
# 
# Best Case Complexity: O(n) - If no element in the list is greater than 5, 
# the inner loop does not execute.
# 
# Worst Case Complexity: O(n^2) - If every element in the list is greater than 5, 
# the inner loop executes fully for each element.
# 
# Average Case Complexity: O(n^2) - Assuming roughly half the elements satisfy the condition, 
# the inner loop still runs frequently.

def processdata(li):
    for i in range(len(li)):  # O(n)
        if li[i] > 5:  # O(1)
            for j in range(len(li)):  # O(n)
                li[i] *= 2  # O(1)

# Question 2: Modify the code so that best, worst, and average case complexities are the same.
# The modified version ensures that every element undergoes the same operation, leading to O(n^2) in all cases.

def processdata_modified(li):
    for i in range(len(li)):  # O(n)
        for j in range(len(li)):  # O(n)
            li[i] *= 2  # O(1)
